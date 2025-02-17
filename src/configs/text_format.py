from enum import Enum, auto

import pygame
pygame.font.init()

from . import Attribute, Config
from ..color.rgb_colors import BLACK

class Justify(Enum):
    """
    Enum representing text justification in widget's text surface.
    """
    LEFT = auto()
    MIDDLE = auto()
    RIGHT = auto()

class TextFormat(Config):
    """
    Class storing text's style data.

    Supported attributes:\n
    name: type = default
    - name: str
    - size: int
    - color: pygame.Color = BLACK
    - bold: bool = False
    - italic: bool = False
    - underline: bool = False
    - strikethrough: bool = False
    - letter_spacing: int = 0
    - line_spacing: int = 0
    - justification: Justify = Justify.LEFT
    """

    name: str
    size: int
    color: pygame.Color
    bold: bool
    italic: bool
    underline: bool
    strikethrough: bool
    letter_spacing: int
    line_spacing: int
    justification: Justify

    attributes: list[Attribute] = [
        Attribute("name", str),
        Attribute("size", int),
        Attribute("color", pygame.Color, BLACK),
        Attribute("bold", bool, False),
        Attribute("italic", bool, False),
        Attribute("underline", bool, False),
        Attribute("strikethrough", bool, False),
        Attribute("letter_spacing", int, 0),
        Attribute("line_spacing", int, 0),
        Attribute("justification", Justify, Justify.LEFT)
    ]
