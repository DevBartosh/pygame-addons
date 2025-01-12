from copy import copy

import pygame

from ..utils.font_utils import FontUtils
from ..configs.text_format import TextFormat, Justify
from ..geometry.surface_aligner import SurfaceAligner
from ..geometry.size import Size
from ..geometry.align import Align

class TextRenderer:
    DEFAULT_TEXT_FORMAT = TextFormat(name="calibri", size=20)

    def __init__(
        self,
        text_format: TextFormat | None = None
    ) -> None:
        self.text_format: TextFormat
        if text_format is None:
            self.text_format = copy(self.DEFAULT_TEXT_FORMAT)
        else:
            self.text_format = text_format
        self.text: str = ""
        self.line: str = ""
        self.text_surface: pygame.Surface | None = None
        self.font: pygame.font.Font

    def render_line(
        self,
        text: str,
        text_format: TextFormat | None = None
    ) -> pygame.Surface:
        self.line = text
        if text_format is not None:
            if self.text_format != text_format:
                self.font = FontUtils.font_from_format(text_format)
                self.text_format = text_format
            used_format = text_format
        else:
            used_format = self.text_format

        line_surface: pygame.Surface
        line_width: int = 0
        dist_from_left: int = 0
        char_surfaces: list[pygame.Surface] = []

        for char in text:
            char_surface = self.font.render(char, 1, used_format.color)
            char_surfaces.append(char_surface)
            line_width += char_surface.get_width()
        
        line_width += (len(text) - 1) * used_format.letter_spacing
        line_surface = pygame.Surface((line_width, used_format.size), pygame.SRCALPHA)

        for index, char_surface in enumerate(char_surfaces):
            line_surface.blit(
                char_surface,
                (dist_from_left, 0)
            )
            spacing = used_format.letter_spacing
            if index == len(char_surfaces) - 1:
                spacing = 0
            dist_from_left += char_surface.get_width() + spacing
        
        assert line_width == dist_from_left

        return line_surface

    def render_text(
        self,
        text: str,
        text_format: TextFormat | None = None
    ) -> pygame.Surface:
        used_format: TextFormat
        if (
            self.text == text and
            self.text_format == text_format and
            self.text_surface is not None
        ):
            return self.text_surface
        
        self.text = text
        if text_format is not None:
            self.text_format = copy(text_format)
            used_format = text_format
            self.font = FontUtils.font_from_format(
                self.text_format
            )
        else:
            used_format = self.text_format

        lines: list[str] = text.split("\n")
        dist_from_top: int = 0
        longest_line_width: int = 0
        line_surfaces: list[pygame.Surface] = []
        line_aligner: SurfaceAligner
        x_line_pos: int
        align_method: Align

        for line in lines:
            line_surface = self.render_line(line, used_format)
            line_surfaces.append(line_surface)
            if line_surface.get_width() > longest_line_width:
                longest_line_width = line_surface.get_width()

        text_height = (
            used_format.size * len(lines) +
            used_format.line_spacing * (len(lines) - 1)
        )
        text_surface = pygame.Surface(
            (
                longest_line_width,
                text_height
            ),
            pygame.SRCALPHA
        )
        line_aligner = SurfaceAligner(
            Size(text_surface.get_width(), text_surface.get_height())
        )
        
        if used_format.justification == Justify.LEFT:
            align_method = Align.TOP_LEFT
        elif used_format.justification == Justify.MIDDLE:
            align_method = Align.TOP_CENTER
        elif used_format.justification == Justify.RIGHT:
            align_method = Align.TOP_RIGHT

        for index, line_surface in enumerate(line_surfaces):
            line_aligner.child_size = Size(
                line_surface.get_width(), line_surface.get_height()
            )
            x_line_pos = line_aligner.get_align_pos(align_method)[0]

            spacing = used_format.line_spacing
            if index == text_surface.get_height():
                spacing = 0
            text_surface.blit(line_surface, (x_line_pos, dist_from_top))
            dist_from_top += used_format.size + spacing
    
        self.text_surface = text_surface
        return self.text_surface