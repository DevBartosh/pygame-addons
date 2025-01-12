from abc import ABC, abstractmethod
from collections.abc import Callable
from copy import copy
from typing import TypeAlias

import pygame

from . import ButtonState
from ..configs import Style, Content
from ..geometry import Position, Size
from ..rendering import ShapeRenderer


class BaseButton(ABC):
    Callback: TypeAlias = Callable[["BaseButton"], None]

    def __init__(
        self,
        position: Position,
        size: Size,
        style: Style,
        content: Content,
        renderer: ShapeRenderer,
        on_press: Callback | None = None,
        on_release: Callback | None = None,
        on_hover: Callback | None = None,
        on_unhover: Callback | None = None,
        on_enable: Callback | None = None,
        on_disable: Callback | None = None,
        on_rest: Callback = lambda button: button.set_rest_surface()
    ) -> None:
        self.rest_size = size
        self.rest_style = style
        self.rest_content = content
        
        self.size = copy(self.rest_size)
        self.style = copy(self.rest_style)
        self.content = copy(self.rest_content)

        self.position = position
        if self.position.surface_aligner is not None:
            self.position.surface_aligner.child_size = self.size
        
        self.renderer = renderer

        self.on_press = on_press
        self.on_release = on_release
        self.on_hover = on_hover
        self.on_unhover = on_unhover
        self.on_enable = on_enable
        self.on_disable = on_disable
        self.on_rest = on_rest
        self.state: ButtonState = ButtonState.REST
        self.disabled = False

        self.surface: pygame.Surface = renderer.get_surface(
            self.size,
            self.style,
            self.content
        )
    
    @abstractmethod
    def update(
        self,
        parent_surface: pygame.Surface,
        mouse_pos: tuple[int, int]
    ) -> None:
        pass

    def set_rest_surface(self) -> None:
        self.size = copy(self.rest_size)
        self.style = copy(self.rest_style)
        self.content = copy(self.rest_content)

    @property
    def disabled(self) -> bool:
        return self.state == ButtonState.DISABLE
    
    @disabled.setter
    def disabled(self, value: bool):
        if value:
            self.state = ButtonState.DISABLE
            if self.on_disable is not None:
                self.on_disable(self)
        else:
            self.state = ButtonState.REST
            if self.on_enable is not None:
                self.on_enable(self)
            self.on_rest(self)