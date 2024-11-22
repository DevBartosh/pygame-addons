from collections.abc import Callable
from typing import Self, TypeAlias
from copy import copy

import pygame

from rendering.button_renderer import ButtonRenderer
from widgets.button_state import ButtonState
from widgets.base_button import BaseButton
from geometry.size import Size
from configs.style import Style
from configs.content import Content
from geometry.position import Position
from color.rgb_colors import *

class ImpulseButton(BaseButton):
    Callback: TypeAlias = Callable[[Self], None]

    def __init__(
        self,
        position: Position,
        size: Size,
        style: Style,
        content: Content,
        renderer: ButtonRenderer, 
        on_press: Callback | None = None,
        on_release: Callback | None = None,
        on_hover: Callback | None = None,
        on_unhover: Callback | None = None,
        on_enable: Callback | None = None,
        on_disable: Callback | None = None
    ) -> None:
        super().__init__(
            position,
            size,
            style,
            content,
            renderer,
            on_press,
            on_release,
            on_hover,
            on_unhover,
            on_enable,
            on_disable
        )
    
    def update(
        self,
        parent_surface: pygame.Surface,
        mouse_pos: tuple[int, int] | None = None
    ) -> None:
        mouse_pos = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]

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
        offset_pos = (
            mouse_pos[0] - self.position.get_x(),
            mouse_pos[1] - self.position.get_y()
        )

        if not self.enabled:
            return
        
        try:
            surface_mask.get_at(offset_pos)
        except IndexError:
            if self.state == ButtonState.HOVER and self.on_unhover is not None:
                self.on_unhover(self)
            self.state = ButtonState.NONE
            self.reset_surface()
            return

        if not surface_mask.get_at(offset_pos):
            return

        if mouse_down:
            if self.state != ButtonState.PRESS:
                self.state = ButtonState.PRESS
                if self.on_press is not None:
                    self.on_press(self)
            return

        if self.state == ButtonState.PRESS:
            if self.on_release is not None:
                self.on_release(self)
        
        if self.state != ButtonState.HOVER:
            self.state = ButtonState.HOVER
            if self.on_hover is not None:
                self.on_hover(self)
        
    def reset_surface(self):
        self.size = copy(self.default_size)
        self.style = copy(self.default_style)
        self.content = copy(self.default_content)