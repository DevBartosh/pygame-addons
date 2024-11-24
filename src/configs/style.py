import pygame

from configs.config import Config
from configs.attribute import Attribute
from color.rgb_colors import TRANSPARENT, BLACK

class Style(Config):
    """
    A class for styling widgets.

    Supported attributes:
    - bg_color: pygame.Color
    - text_color: pygame.Color
    - text_font: pygame.font.Font
    - border_color: pygame.Color
    - border_width: int
    - border_radius: int
    - bg_image: pygame.Surface
    """

    bg_color: pygame.Color
    text_color: pygame.Color
    text_font: pygame.font.Font
    border_color: pygame.Color
    border_width: int
    border_radius: int
    bg_image: pygame.Surface

    attributes: list[Attribute] = [
        Attribute("bg_color", pygame.Color, TRANSPARENT),
        Attribute("text_font", pygame.font.Font, pygame.font.SysFont("calibri", 20)),
        Attribute("text_color", pygame.Color, BLACK),
        Attribute("border_color", pygame.Color, TRANSPARENT),
        Attribute("border_width", int, 0),
        Attribute("border_radius", int, 0),
        Attribute("bg_image", pygame.Surface, pygame.Surface((0, 0)))
    ]