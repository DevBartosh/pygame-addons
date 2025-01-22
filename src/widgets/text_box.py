import pygame

from ..configs import Style, Content
from ..geometry import Size, Position, AutoSize
from ..rendering import ShapeRenderer

class TextBox:
    def __init__(
        self,
        position: Position,
        size: Size,
        style: Style,
        content: Content,
        renderer: ShapeRenderer
    ):
        self.position = position
        self.size = size
        self.style = style
        self.content = content
        self.renderer = renderer
        self.surface = self.renderer.get_surface(
            self.size,
            self.style,
            self.content
        )
        if isinstance(self.size, AutoSize):
            self.size.set_width = self.surface.get_width()
            self.size.set_height = self.surface.get_height()
    
    def update(
        self,
        parent_surface: pygame.Surface
    ):
        surface: pygame.Surface = self.renderer.get_surface(
            self.size,
            self.style,
            self.content
        )
        if isinstance(self.size, AutoSize):
            self.size.set_width = self.surface.get_width()
            self.size.set_height = self.surface.get_height()

        parent_surface.blit(surface, self.position.get_tuple())