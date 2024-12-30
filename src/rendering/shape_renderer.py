from abc import ABC, abstractmethod

import pygame

from geometry.size import Size
from configs.style import Style
from configs.content import Content

class ShapeRenderer(ABC):
    """
    Base class for widget renderers.
    """
    def __init__(self) -> None:
        self.style: Style | None = None
        self.size: Size | None = None
        self.content: Content | None = None
        self.surface: pygame.Surface
    
    @abstractmethod
    def get_surface(
        self,
        size: Size,
        style: Style,
        content: Content
    ) -> pygame.Surface:
        pass