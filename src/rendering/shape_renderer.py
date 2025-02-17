from abc import ABC, abstractmethod

import pygame

from ..geometry import Size
from ..configs import Style, Content

class ShapeRenderer(ABC):
    """
    Base class for simple widget renderers.
    """
    def __init__(self) -> None:
        self.previous_data_hash: str = ""
        self.surface: pygame.Surface | None = None
    
    @abstractmethod
    def get_surface(
        self,
        size: Size,
        style: Style,
        content: Content
    ) -> pygame.Surface:
        pass