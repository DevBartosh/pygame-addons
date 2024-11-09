import pygame

from config import Config
from position import Position
from size import Size
from attribute import Attribute

class Content(Config):
    """
    A class made for storing widget's content.

    Supported attributes:
    - text: str
    - text_color: pygame.Color
    - text_font: pygame.font.Font
    - text_position: Position
    - secondary_text: str
    - image: pygame.Surface
    - image_size: Size
    - image_position: Position
    """

    attributes: list[Attribute] = [
        Attribute("text", str, ""),
        Attribute("text_font", pygame.font.Font),
        Attribute("text_color", pygame.Color),
        Attribute("text_position", Position, Position()),
        Attribute("secondary_text", str, ""),
        Attribute("image", pygame.Surface, pygame.Surface((0, 0))),
        Attribute("image_size", Size, Size(0, 0)),
        Attribute("image_position", Position, Position())
    ]
