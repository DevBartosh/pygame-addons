from collections.abc import Callable
from typing import Self, TypeAlias

import pygame

from configs.content import Content
from configs.style import Style
from geometry.size import Size
from geometry.position import Position
from rendering.button_renderer import ButtonRenderer
from widgets.button_state import ButtonState
from widgets.base_button import BaseButton

class Button(BaseButton):
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
        on_disable: Callback | None = None,
        on_rest: Callback | None = lambda button: button.set_rest_surface(),
        spam_on_hover: bool = False,
        spam_on_press: bool = False,
        spam_on_rest: bool = False
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
            on_disable,
            on_rest
        )
        self.spam_on_hover = spam_on_hover
        self.spam_on_press = spam_on_press
        self.spam_on_rest = spam_on_rest
    
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

        if self.disabled:
            return
        
        try:
            surface_mask.get_at(offset_pos)
        except IndexError:
            if (
                self.state == ButtonState.HOVER or
                self.state == ButtonState.PRESS or
                self.spam_on_rest
            ):
                self.on_rest(self)
                if self.on_unhover is not None:
                    self.on_unhover(self)
            self.state = ButtonState.REST
            return

        if not surface_mask.get_at(offset_pos):
            return

        if mouse_down:
            if self.state != ButtonState.PRESS or self.spam_on_press:
                self.state = ButtonState.PRESS
                if self.on_press is not None:
                    self.on_press(self)
            return

        if self.state == ButtonState.PRESS:
            if self.on_release is not None:
                self.on_release(self)
        
        if self.state != ButtonState.HOVER or self.spam_on_hover:
            self.state = ButtonState.HOVER
            if self.on_hover is not None:
                self.on_hover(self)
            else:
                self.on_rest(self)