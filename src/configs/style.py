import pygame
import os
print(os.getcwd())

from configs.config import Config
from configs.attribute import Attribute
from rgb_colors import TRANSPARENT

class Style(Config):
    """
    A class for styling widgets.

    Supported attributes:
    - bg_color: pygame.Color
    - border_color: pygame.Color
    - border_width: int
    - border_radius: int
    - bg_image: pygame.Surface
    """

    bg_color: pygame.Color
    border_color: pygame.Color
    border_width: int
    border_radius: int
    bg_image: pygame.Surface

    attributes: list[Attribute] = [
        Attribute("bg_color", pygame.Color, TRANSPARENT),
        Attribute("border_color", pygame.Color, TRANSPARENT),
        Attribute("border_width", int, 0),
        Attribute("border_radius", int, 0),
        Attribute("bg_image", pygame.Surface, pygame.Surface((0, 0)))
    ]