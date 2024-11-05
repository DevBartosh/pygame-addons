import pygame

from config import Config
from position import Position
from size import Size
from attribute import Attribute

class Content(Config):
    """
    A class made for storing widget's content.

    Supported attributes:
    - image: pygame.Surface
    - image_size: Size
    - image_position: Position
    - text: str
    - text_color: pygame.Color
    - text_font: pygame.font.Font
    - text_position: Position
    - secondary_text: str

    A widget doesn't need any of this to work.
    """

    attributes: list[Attribute] = [
        Attribute("text", str, ""),
        Attribute("text_font", pygame.font.Font),
        Attribute("text_color", pygame.Color),
        Attribute("text_position", Position),
        Attribute("secondary_text", str, ""),
        Attribute("image", pygame.Surface),
        Attribute("image_size", Size),
        Attribute("image_position", Position)
    ]
