import pygame
pygame.font.init()

from .config import Config
from ..geometry.position import Position
from .attribute import Attribute

class Content(Config):
    """
    A class made for storing widget's content.

    Supported attributes:
    - text: str
    - text_position: Position
    - text_2: str
    - text_2_position: Position
    - image: pygame.Surface
    - image_position: Position
    """
    
    text: str
    text_position: Position
    text_2: str
    text_2_position: Position
    image: pygame.Surface
    image_position: Position

    attributes: list[Attribute] = [
        Attribute("text", str, ""),
        Attribute("text_position", Position, Position()),
        Attribute("text_2", str, ""),
        Attribute("text_2_position", Position, Position()),
        Attribute("image", pygame.Surface, pygame.Surface((0, 0))),
        Attribute("image_position", Position, Position())
    ]
