from pygame.surface import Surface as Surface
from configs.content import Content
from configs.style import Style
from geometry.size import Size
from rendering.renderer import Renderer

class ButtonRenderer(Renderer):
    def __init__(self) -> None:
        super().__init__()
    
    def get_surface(
        self,
        size: Size,
        style: Style,
        content: Content
    ) -> Surface:
        return super().get_surface(size, style, content)