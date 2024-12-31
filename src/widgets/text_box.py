import pygame

from ..configs.content import Content
from ..configs.style import Style
from ..geometry.size import Size
from ..geometry.position import Position
from ..rendering.shape_renderer import ShapeRenderer

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
    
    def update(
        self,
        parent_surface: pygame.Surface
    ):
        surface: pygame.Surface = self.renderer.get_surface(
            self.size,
            self.style,
            self.content
        )

        parent_surface.blit(surface, self.position.get_tuple())