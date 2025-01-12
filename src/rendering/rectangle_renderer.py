from copy import copy

import pygame

from . import ShapeRenderer, TextRenderer
from ..configs import Style, Content
from ..geometry import Size
from ..utils import SurfaceUtils

class RectangleRenderer(ShapeRenderer):
    def __init__(self) -> None:
        super().__init__()
        self.text_renderer = TextRenderer()

    def get_surface(
        self,
        size: Size,
        style: Style,
        content: Content
    ) -> pygame.Surface:
        if (
            self.size == size and
            self.style == style and
            self.content == content and
            self.surface is not None
        ):
            return self.surface

        self.size = copy(size)
        self.style = copy(style)
        self.content = copy(content)

        surface = pygame.Surface(size.get_tuple(), pygame.SRCALPHA)
        button_rect = pygame.Rect((0, 0), size.get_tuple())

        pygame.draw.rect(
            surface,
            style.bg_color,
            button_rect,
            border_radius=style.border_radius
        )

        if style.border_width != 0:
            pygame.draw.rect(
                surface,
                style.border_color,
                button_rect,
                style.border_width,
                style.border_radius
            )
        if not SurfaceUtils.surfaces_equal(style.bg_image, pygame.Surface((0, 0))):
            surface.blit(
                style.bg_image,
                (0, 0),
                button_rect
            )

        if content.text != "":
            text_surface: pygame.Surface = self.text_renderer.render_text(
                content.text,
                style.text_format
            )
            
            if content.text_position.surface_aligner is not None:
                content.text_position.surface_aligner.child_size = Size(
                    text_surface.get_width(),
                    text_surface.get_height()
                )
            surface.blit(
                text_surface,
                content.text_position.get_tuple(),
                button_rect
            )
        
        if not SurfaceUtils.surfaces_equal(content.image, pygame.Surface((0, 0))):
            if content.image_position.surface_aligner is not None:
                content.image_position.surface_aligner.child_size = Size(
                    content.image.get_width(),
                    content.image.get_height()
                )
            surface.blit(
                content.image,
                content.image_position.get_tuple(),
                button_rect
            )

        self.surface = surface
        return self.surface

    