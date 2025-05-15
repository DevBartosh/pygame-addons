import pygame

from . import ButtonState, BaseButton
from ..configs import Style, Content
from ..geometry import Size, Position
from ..rendering import ShapeRenderer

class Button(BaseButton):
    """
    Button widget with much customizability and many types of callbacks.
    """
    def __init__(
        self,
        position: Position,
        size: Size,
        style: Style,
        content: Content,
        renderer: ShapeRenderer,
        on_press: BaseButton.Callback | None = None,
        on_release: BaseButton.Callback | None = None,
        on_hover: BaseButton.Callback | None = None,
        on_unhover: BaseButton.Callback | None = None,
        on_enable: BaseButton.Callback | None = None,
        on_disable: BaseButton.Callback | None = None,
        on_rest: BaseButton.Callback = lambda button: button.set_rest_surface(),
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
        if mouse_pos is None:
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