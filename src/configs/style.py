import pygame

from configs.config import Config
from configs.attribute import Attribute
from color.rgb_colors import TRANSPARENT
from configs.text_format import TextFormat

class Style(Config):
    """
    A class for styling widgets.

    Supported attributes:
    - bg_color: pygame.Color
    - border_color: pygame.Color
    - border_width: int
    - border_radius: int
    - text_format: TextFormat
    - bg_image: pygame.Surface
    """

    bg_color: pygame.Color
    border_color: pygame.Color
    border_width: int
    border_radius: int
    text_format: TextFormat
    bg_image: pygame.Surface

    attributes: list[Attribute] = [
        Attribute("bg_color", pygame.Color, TRANSPARENT),
        Attribute("border_color", pygame.Color, TRANSPARENT),
        Attribute("border_width", int, 0),
        Attribute("border_radius", int, 0),
        Attribute("text_format", TextFormat, TextFormat(name="calibri", size=40)),
        Attribute("bg_image", pygame.Surface, pygame.Surface((0, 0)))
    ]