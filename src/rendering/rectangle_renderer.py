import pygame

from ..configs.style import Style
from ..configs.content import Content
from ..geometry.size import Size
from .shape_renderer import ShapeRenderer
from .text_renderer import TextRenderer

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
        """
        TODO:
        The problem with this is that content and style have Surface objects that cannot be easily compared like Size object.
        I have solved this problem in TextRenderer, because the attributes there are simple literals like strings and ints

        if (
            self.size == size and
            self.style == style and
            self.content == content and
            self.surface is not None
        ):
            return self.surface
        else:
            print("Size: " + str(self.size == size))
            print("Style: " + str(self.style == style))
            print("Content: " + str(self.content == content))
            self.size = size
            self.style = style
            self.content = content
        """
        self.size = size
        self.style = style
        self.content = content

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
        if style.bg_image != pygame.Surface((0, 0)):
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
        
        if content.image != pygame.Surface((0, 0)):
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

    