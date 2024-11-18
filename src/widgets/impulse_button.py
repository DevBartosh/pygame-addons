from collections.abc import Callable
from typing import Self

import pygame

from rendering.button_renderer import ButtonRenderer
from widgets.button import Button
from geometry.size import Size
from configs.style import Style
from configs.content import Content
from geometry.position import Position
from color.rgb_colors import *

class ImpulseButton(Button):
    def __init__(
        self,
        position: Position,
        size: Size,
        style: Style,
        content: Content,
        renderer: ButtonRenderer,
        disabled: bool = False,
        on_click: Callable[[Self], None] | None = None,
        on_hover: Callable[[Self], None] | None = None,
        on_disable: Callable[[Self], None] | None = None,
        on_rest: Callable[[Self], None] | None = None
    ) -> None:
        super().__init__(
            position,
            size,
            style, 
            content,
            renderer,
            disabled,
            on_click,
            on_hover,
            on_disable,
            on_rest
        )
        self.clicked: bool = False
    
    def update(
        self,
        parent_surface: pygame.Surface,
        mouse_pos: tuple[int, int] | None = None
    ) -> None:
        mouse_pos = pygame.mouse.get_pos()

        self.surface = self.renderer.get_surface(
            self.size,
            self.style,
            self.content
        )

        parent_surface.blit(
            self.surface,
            self.position.get_tuple(),
            pygame.Rect((0, 0), self.size.get_tuple())
        )

        surface_mask: pygame.Mask = pygame.mask.from_surface(self.surface)
        offset_x = mouse_pos[0] - self.position.get_x()
        offset_y = mouse_pos[1] - self.position.get_y()

        if self.disabled:
            if self.on_disable is not None:
                self.on_disable(self)
            return

        try:
            surface_mask.get_at((offset_x, offset_y))
        except IndexError:
            if self.on_rest is not None:
                self.on_rest(self)
            return
        
        if pygame.mouse.get_pressed()[0] and self.on_click is not None and not self.clicked:
            self.on_click(self)
            self.clicked = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            if self.on_hover is not None:
                self.on_hover(self)            
        




        
