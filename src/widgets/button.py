from collections.abc import Callable
from typing import Self
from abc import ABC, abstractmethod

import pygame

from geometry.position import Position
from geometry.size import Size
from configs.style import Style
from configs.content import Content
from rendering.button_renderer import ButtonRenderer


class Button(ABC):
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
        self.position = position
        if self.position.surface_aligner is not None:
            self.position.surface_aligner.child_size = size
        self.size = size
        self.style = style
        self.content = content
        self.renderer = renderer
        self.disabled = disabled
        self.on_click = on_click
        self.on_hover = on_hover
        self.on_disable = on_disable
        self.on_rest = on_rest
        self.surface: pygame.Surface = renderer.get_surface(
            self.size,
            self.style,
            self.content
        )
    
    @abstractmethod
    def update(
        parent_surface: pygame.Surface,
        mouse_pos: tuple[int, int]
    ) -> None:
        pass