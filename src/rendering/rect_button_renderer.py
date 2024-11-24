import pygame

from configs.style import Style
from configs.content import Content
from geometry.size import Size
from rendering.button_renderer import ButtonRenderer

class RectButtonRenderer(ButtonRenderer):
    def __init__(self) -> None:
        super().__init__()

    def get_surface(
        self,
        size: Size,
        style: Style,
        content: Content
    ) -> pygame.Surface:
        
        if self.current_size is None:
            self.current_size = size
        if self.current_style is None:
            self.current_style = style
        if self.current_content is None:
            self.current_content = content

        self.surface = pygame.Surface(size.get_tuple(), pygame.SRCALPHA)
        button_rect = pygame.Rect((0, 0), size.get_tuple())

        pygame.draw.rect(
            self.surface,
            style.bg_color,
            button_rect,
            border_radius=style.border_radius
        )

        if style.border_width != 0:
            pygame.draw.rect(
                self.surface,
                style.border_color,
                button_rect,
                style.border_width,
                style.border_radius
            )

        self.surface.blit(
            style.bg_image,
            (0, 0),
            button_rect
        )

        if content.text != "":
            text_surface: pygame.Surface = style.text_font.render(
                content.text,
                True,
                style.text_color
            )

            if content.text_position.surface_aligner is not None:
                content.text_position.surface_aligner.child_size = Size(
                    text_surface.get_width(),
                    text_surface.get_height()
                )
            self.surface.blit(
                text_surface,
                content.text_position.get_tuple(),
                button_rect
            )
        
        if content.image != pygame.Surface((0, 0)):
            if content.image_position.surface_aligner is not None:
                content.image_position.surface_aligner.child_size = Size(
                    content.image.get_width(),
                    content.image.get_height()
                )
            self.surface.blit(
                content.image,
                content.image_position.get_tuple(),
                button_rect
            )
        
        return self.surface

    