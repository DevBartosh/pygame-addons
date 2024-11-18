import pygame
pygame.font.init()

from configs.config import Config
from geometry.position import Position
from configs.attribute import Attribute
from color.rgb_colors import BLACK

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
    - image_position: Position
    """
    
    text: str
    text_font: pygame.font.Font
    text_color: pygame.Color
    text_position: Position
    secondary_text: str
    image: pygame.Surface
    image_position: Position

    attributes: list[Attribute] = [
        Attribute("text", str, ""),
        Attribute("text_font", pygame.font.Font, pygame.font.SysFont("calibri", 20)),
        Attribute("text_color", pygame.Color, BLACK),
        Attribute("text_position", Position, Position()),
        Attribute("secondary_text", str, ""),
        Attribute("image", pygame.Surface, pygame.Surface((0, 0))),
        Attribute("image_position", Position, Position())
    ]
