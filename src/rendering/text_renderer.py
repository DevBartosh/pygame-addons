from copy import copy
from hashlib import sha256

import pygame

from ..utils.font import font_from_format
from ..configs import TextFormat, Justify
from ..geometry import SurfaceAligner, Size, Align, AutoSize

class TextRenderer:
    """
    Class generating a text surface based on a given text format.
    """
    DEFAULT_TEXT_FORMAT = TextFormat(name="calibri", size=20)

    def __init__(self) -> None:
        self.previous_data_hash: str = ""
        self.text_surface: pygame.Surface | None = None

    def get_data_hash(self, text: str, text_format: TextFormat) -> str:
        return sha256(f"{text} {text_format}".encode()).hexdigest()

    def render_line(
        self,
        text: str,
        text_format: TextFormat
    ) -> pygame.Surface:
        self.font = font_from_format(text_format)

        line_surface: pygame.Surface
        line_width: int = 0
        dist_from_left: int = 0
        char_surfaces: list[pygame.Surface] = []
        spacing: int

        for index, char in enumerate(text):
            char_surface = self.font.render(char, 1, text_format.color)
            char_surfaces.append(char_surface)
            spacing = text_format.letter_spacing
            if index == len(text) - 1:
                spacing = 0
            line_width += char_surface.get_width() + spacing
        
        line_surface = pygame.Surface((line_width, text_format.size), pygame.SRCALPHA)

        for index, char_surface in enumerate(char_surfaces):
            line_surface.blit(
                char_surface,
                (dist_from_left, 0)
            )
            spacing = text_format.letter_spacing
            if index == len(char_surfaces) - 1:
                spacing = 0
            dist_from_left += char_surface.get_width() + spacing

        return line_surface

    def render_text(
        self,
        text: str,
        text_format: TextFormat
    ) -> pygame.Surface:
        data_hash: str = self.get_data_hash(text, text_format)
        if (
            data_hash == self.previous_data_hash and
            self.text_surface is not None
        ):
            return self.text_surface
        else:
            self.previous_data_hash = data_hash

        lines: list[str] = text.split("\n")
        dist_from_top: int = 0
        longest_line_width: int = 0
        text_height: int = 0
        line_surfaces: list[pygame.Surface] = []
        line_aligner: SurfaceAligner
        line_x_pos: int
        align_method: Align

        for index, line in enumerate(lines):
            line_surface = self.render_line(line, text_format)
            line_surfaces.append(line_surface)

            spacing = text_format.line_spacing
            if index == len(lines) - 1:
                spacing = 0
            text_height += text_format.size + spacing
        
        longest_line_width = max(map(lambda surf: surf.get_width(), line_surfaces))
            
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
        
        if text_format.justification == Justify.LEFT:
            align_method = Align.TOP_LEFT
        elif text_format.justification == Justify.MIDDLE:
            align_method = Align.TOP_CENTER
        elif text_format.justification == Justify.RIGHT:
            align_method = Align.TOP_RIGHT

        for index, line_surface in enumerate(line_surfaces):
            if isinstance(line_aligner.child_size, AutoSize):
                line_aligner.child_size.set_width = line_surface.get_width()
                line_aligner.child_size.set_height = line_surface.get_height()
            line_x_pos = line_aligner.get_align_pos(align_method)[0]

            spacing = text_format.line_spacing
            if index == text_surface.get_height():
                spacing = 0
            text_surface.blit(line_surface, (line_x_pos, dist_from_top))
            dist_from_top += text_format.size + spacing
    
        self.text_surface = text_surface
        return self.text_surface