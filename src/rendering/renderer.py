from abc import ABC, abstractmethod

import pygame

from geometry.size import Size
from configs.style import Style
from configs.content import Content

class Renderer(ABC):
    """
    Base class for widget renderers.
    """
    def __init__(self) -> None:
        self.current_style: Style | None = None
        self.current_size: Size | None = None
        self.current_content: Content | None = None
        self.surface: pygame.Surface
    
    @abstractmethod
    def get_surface(
        self,
        size: Size,
        style: Style,
        content: Content
    ) -> pygame.Surface:
        pass