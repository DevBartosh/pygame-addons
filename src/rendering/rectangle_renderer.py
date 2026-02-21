from copy import copy
from hashlib import sha256

import pygame

from . import ShapeRenderer, TextRenderer
from ..configs import Style, Content
from ..geometry import Size, AutoSize

class RectangleRenderer(ShapeRenderer):
    """
    Class generating a rectangular surface based on size, style and content.
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.text_1_renderer = TextRenderer()
        self.text_2_renderer = TextRenderer()

    def get_data_hash(self, size: Size, style: Style, content: Content) -> str:
        return sha256(f"{str(size)} {str(style)} {str(content)}".encode()).hexdigest()

    def get_surface(
        self,
        size: Size,
        style: Style,
        content: Content
    ) -> pygame.Surface:
        data_hash: str = self.get_data_hash(size, style, content)
        if (
            data_hash == self.previous_data_hash and
            self.surface is not None
        ):
            return self.surface
        else:
            self.previous_data_hash = data_hash

        text_1_surface: pygame.Surface
        text_2_surface: pygame.Surface
        surface: pygame.Surface
        button_rect: pygame.Rect
        text_position_child_size: Size | AutoSize
        text_2_position_child_size: Size | AutoSize
        image_position_child_size: Size | AutoSize

        text_1_surface = self.text_1_renderer.render_text(
            content.text,
            style.text_format
        )
        if content.text_position.surface_aligner is not None:
            text_position_child_size = content.text_position.surface_aligner.child_size
            if isinstance(text_position_child_size, AutoSize):
                if text_position_child_size.width_auto_setting:
                    text_position_child_size.set_width = text_1_surface.get_width()
                if text_position_child_size.height_auto_setting:
                    text_position_child_size.set_height = text_1_surface.get_height()
        
        text_2_surface = self.text_2_renderer.render_text(
            content.text_2,
            style.text_format
        )
        if content.text_2_position.surface_aligner is not None:
            text_2_position_child_size = content.text_2_position.surface_aligner.child_size
            if isinstance(text_2_position_child_size, AutoSize):
                if text_2_position_child_size.width_auto_setting:
                    text_2_position_child_size.set_width = text_2_surface.get_width()
                if text_2_position_child_size.height_auto_setting:
                    text_2_position_child_size.set_height = text_2_surface.get_height()

        if content.image_position.surface_aligner is not None:
            image_position_child_size = content.image_position.surface_aligner.child_size
            if isinstance(image_position_child_size, AutoSize):
                if image_position_child_size.width_auto_setting:
                    image_position_child_size.set_width = content.image.get_width()
                if image_position_child_size.height_auto_setting:
                    image_position_child_size.set_height = content.image.get_height()

        surface = pygame.Surface(size.to_tuple(), pygame.SRCALPHA)
        button_rect = pygame.Rect((0, 0), size.to_tuple())

        pygame.draw.rect(
            surface,
            style.bg_color,
            button_rect,
            border_radius=style.border_radius
        )
        surface.blit(style.bg_image, (0, 0))
        if style.border_width != 0:
            pygame.draw.rect(
                surface,
                style.border_color,
                button_rect,
                style.border_width,
                style.border_radius
            )
        surface.blit(text_1_surface, content.text_position.to_tuple())
        surface.blit(text_2_surface, content.text_2_position.to_tuple())
        surface.blit(content.image, content.image_position.to_tuple())

        self.surface = surface
        return self.surface

    