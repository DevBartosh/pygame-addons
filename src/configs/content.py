import pygame
pygame.font.init()

from . import Attribute, Config
from ..geometry import Position

class Content(Config):
    """
    Class storing widget's content data.

    Supported attributes:\n
    name: type = default
    - text: str
    - text_position: Position = Position(0, 0)
    - text_2: str = ""
    - text_2_position: Position = Position(0, 0)
    - image: pygame.Surface = pygame.Surface((0, 0))
    - image_position: Position = Position(0, 0)
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
