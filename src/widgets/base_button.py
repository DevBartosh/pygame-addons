from abc import ABC, abstractmethod
from collections.abc import Callable
from copy import copy
from typing import Self, TypeAlias

import pygame

from configs.content import Content
from configs.style import Style
from geometry.position import Position
from geometry.size import Size
from rendering.button_renderer import ButtonRenderer
from widgets.button_state import ButtonState


class BaseButton(ABC):
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
        on_rest: Callback | None = None
    ) -> None:
        self.position = position
        if self.position.surface_aligner is not None:
            self.position.surface_aligner.child_size = size
        
        self.default_size = size
        self.default_style = style
        self.default_content = content
        
        self.size = copy(self.default_size)
        self.style = copy(self.default_style)
        self.content = copy(self.default_content)
        
        self.renderer = renderer

        self.on_press = on_press
        self.on_release = on_release
        self.on_hover = on_hover
        self.on_unhover = on_unhover
        self.on_enable = on_enable
        self.on_disable = on_disable
        self.on_rest = on_rest
        self.state: ButtonState = ButtonState.REST

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

    def set_default_surface(self):
        self.size = copy(self.default_size)
        self.style = copy(self.default_style)
        self.content = copy(self.default_content)

    @property
    def enabled(self) -> bool:
        return self.state != ButtonState.DISABLE
    
    @enabled.setter
    def enabled(self, value: bool):
        if value:
            self.state = ButtonState.REST
            if self.on_enable is not None:
                self.on_enable(self)
            self.set_default_surface()
        else:
            self.state = ButtonState.DISABLE
            if self.on_disable is not None:
                self.on_disable(self)