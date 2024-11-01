import pygame

from config import Config

class Style(Config):
    """
    A class for styling widgets.

    Supported attributes:
    - bg_color: pygame.Color
    - border_color: pygame.Color
    - border_width: int
    - border_radius: int
    - bg_image: pygame.Surface

    A widget needs only bg_color attribute to be seen.
    """
    
    allowed_attributes: dict = {
        "bg_color": pygame.Color,
        "border_color": pygame.Color,
        "border_width": int,
        "border_radius": int,
        "bg_image": pygame.Surface
    }