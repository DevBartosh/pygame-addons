import pygame
pygame.font.init()
from ..configs.text_format import TextFormat

class FontUtils:
    @staticmethod
    def font_from_data(
        name: str,
        size: int,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        strikethrough: bool = False
    ) -> pygame.font.Font:
        if name.lower() in pygame.font.get_fonts():
            font = pygame.font.SysFont(name.lower(), size, bold, italic)
        else:
            font = pygame.font.Font(name, size)
            font.set_bold(bold)
            font.set_italic(italic)

        font.set_underline(underline)
        font.set_strikethrough(strikethrough)

        return font

    @staticmethod
    def font_from_format(text_format: TextFormat) -> pygame.font.Font:
        return FontUtils.font_from_data(
            text_format.name,
            text_format.size,
            text_format.bold,
            text_format.italic,
            text_format.underline,
            text_format.strikethrough
        )
    
    