import pygame

from . import Attribute, Config, TextFormat
from ..color.rgb_colors import TRANSPARENT

class Style(Config):
    """
    Class storing widget's style data.

    Supported attributes:\n
    name: type = default
    - bg_color: pygame.Color = TRANSPARENT
    - border_color: pygame.Color = TRANSPARENT
    - border_width: int = 0
    - border_radius: int = 0
    - text_format: TextFormat = TextFormat(name="calibri", size=40)
    - bg_image: pygame.Surface = pygame.Surface((0, 0))
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