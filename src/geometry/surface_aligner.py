from .size import Size
from .align import Align

class SurfaceAligner:
    """
    Class containing parent surface size and child surface size for centering purposes.
    """
    def __init__(self,
        parent_surface_size: Size,
        child_surface_size: Size = Size(0, 0)
    ) -> None:
        self.parent_size = parent_surface_size
        self.child_size = child_surface_size
    
    def get_centered_x(self, child_width_overwrite: int | None = None) -> int:
        parent_width = self.parent_size.width
        child_width = self.child_size.width

        if child_width_overwrite is not None:
            child_width = child_width_overwrite
        
        return (parent_width - child_width) // 2
    
    def get_centered_y(self, child_height_overwrite: int | None = None) -> int:
        parent_height = self.parent_size.height
        child_height = self.child_size.height

        if child_height_overwrite is not None:
            child_height = child_height_overwrite
        
        return (parent_height - child_height) // 2
    
    def get_centered_pos(
        self,
        child_width_overwrite: int | None = None,
        child_height_overwrite: int | None = None
    ) -> tuple[int, int]:
        return (
            self.get_centered_x(child_width_overwrite),
            self.get_centered_y(child_height_overwrite)
        )
    
    def get_align_pos(self, align: Align) -> tuple[int, int]:
        match align:
            case Align.TOP_LEFT | Align.NONE:
                x = 0
                y = 0
            case Align.TOP_CENTER:
                x = self.get_centered_x()
                y = 0
            case Align.TOP_RIGHT:
                x = self.parent_size.width - self.child_size.width
                y = 0
            case Align.CENTER_LEFT:
                x = 0
                y = self.get_centered_y()
            case Align.CENTER:
                x = self.get_centered_x()
                y = self.get_centered_y()
            case Align.CENTER_RIGHT:
                x = self.parent_size.width - self.child_size.width
                y = self.get_centered_y()
            case Align.BOTTOM_LEFT:
                x = 0
                y = self.parent_size.height - self.child_size.height
            case Align.BOTTOM_CENTER:
                x = self.get_centered_x()
                y = self.parent_size.height - self.child_size.height
            case Align.BOTTOM_RIGHT:
                x = self.parent_size.width - self.child_size.width
                y = self.parent_size.height - self.child_size.height
        
        return (x, y)
    

    
