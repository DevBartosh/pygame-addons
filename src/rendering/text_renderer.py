from copy import copy

import pygame

from utils.font_utils import FontUtils
from configs.text_format import TextFormat, Justify
from geometry.surface_aligner import SurfaceAligner
from geometry.size import Size
from geometry.align import Align

class TextRenderer:
    DEFAULT_TEXT_FORMAT = TextFormat(name="calibri", size=20)

    def __init__(self) -> None:
        self.text_format: TextFormat = copy(self.DEFAULT_TEXT_FORMAT)
        self.text: str = ""
        self.text_surface: pygame.Surface | None = None
        self.font: pygame.font.Font

    def render_line(self, text: str, text_format: TextFormat | None = None) -> pygame.Surface:
        line_font: pygame.font.Font
        line_format: TextFormat
        if text_format is None or text_format == self.text_format:
            line_font = self.font
            line_format = self.text_format
        else:
            line_font = FontUtils.font_from_format(text_format)
            line_format = text_format
        line_surface: pygame.Surface
        line_width: int = 0
        dist_from_left: int = 0
        char_surfaces: list[pygame.Surface] = []

        for char in text:
            char_surface = line_font.render(char, 1, line_format.color)
            char_surfaces.append(char_surface)
            line_width += char_surface.get_width()
        
        line_width += (len(text) - 1) * line_format.letter_spacing
        line_surface = pygame.Surface((line_width, self.text_format.size), pygame.SRCALPHA)

        for index, char_surface in enumerate(char_surfaces):
            line_surface.blit(
                char_surface,
                (dist_from_left, 0)
            )
            spacing = self.text_format.letter_spacing
            if index == len(char_surfaces) - 1:
                spacing = 0
            dist_from_left += char_surface.get_width() + spacing
        
        assert line_width == dist_from_left

        return line_surface

    def render_text(self, text: str, text_format: TextFormat) -> pygame.Surface:
        if self.text_format == self.DEFAULT_TEXT_FORMAT:
            self.text_format = text_format
        if self.text == "":
            self.text = text

        if (
            self.text == text and
            self.text_format == text_format and
            self.text_surface is not None
        ):
            return self.text_surface
        else:
            self.text = text
            self.text_format = text_format

        self.font = FontUtils.font_from_format(
            self.text_format
        )
        lines: list[str] = text.split("\n")
        dist_from_top: int = 0
        longest_line_width: int = 0
        line_surfaces: list[pygame.Surface] = []
        line_aligner: SurfaceAligner
        x_line_pos: int
        align_method: Align

        for line in lines:
            line_surface = self.render_line(line)
            line_surfaces.append(line_surface)
            if line_surface.get_width() > longest_line_width:
                longest_line_width = line_surface.get_width()

        text_surface = pygame.Surface(
            (
                longest_line_width,
                self.text_format.size * len(lines) + self.text_format.line_spacing * (len(lines) - 1)
            ),
            pygame.SRCALPHA
        )
        line_aligner = SurfaceAligner(
            Size(text_surface.get_width(), text_surface.get_height())
        )
        
        if self.text_format.justification == Justify.LEFT:
            align_method = Align.TOP_LEFT
        elif self.text_format.justification == Justify.MIDDLE:
            align_method = Align.TOP_CENTER
        elif self.text_format.justification == Justify.RIGHT:
            align_method = Align.TOP_RIGHT

        for index, line_surface in enumerate(line_surfaces):
            line_aligner.child_size = Size(
                line_surface.get_width(), line_surface.get_height()
            )
            x_line_pos = line_aligner.get_align_pos(align_method)[0]

            spacing = self.text_format.line_spacing
            if index == text_surface.get_height():
                spacing = 0
            text_surface.blit(line_surface, (x_line_pos, dist_from_top))
            dist_from_top += self.text_format.size + spacing
    
        self.text_surface = text_surface
        return self.text_surface