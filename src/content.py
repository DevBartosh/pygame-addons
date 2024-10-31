import pygame

from config import Config
from position import Position
from size import Size

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

    attributes_and_types: dict = {
        "image": pygame.Surface,
        "image_size": Size,
        "image_position": Position,
        "text": str,
        "text_font": pygame.font.Font,
        "text_color": pygame.Color,
        "text_position": Position,
        "secondary_text": str
    }
