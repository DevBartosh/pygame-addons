from size import Size
from align import Align

class SurfaceAligner:
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
    
    def get_align_pos(self, align: Align) -> tuple[int, int]:
        match align:
            case Align.TOP_LEFT | Align.CENTER_LEFT | Align.BOTTOM_LEFT:
                x = 0
            case Align.TOP_CENTER | Align.CENTER | Align.BOTTOM_CENTER:
                x = self.get_centered_x()
            case Align.TOP_RIGHT | Align.CENTER_RIGHT | Align.BOTTOM_RIGHT:
                x = self.parent_size.width - self.child_size.width
        
        match align:
            case Align.TOP_LEFT | Align.TOP_CENTER | Align.TOP_RIGHT:
                y = 0
            case Align.CENTER_LEFT | Align.CENTER | Align.CENTER_RIGHT:
                y = self.get_centered_y()
            case Align.BOTTOM_LEFT | Align.BOTTOM_CENTER | Align.BOTTOM_RIGHT:
                y = self.parent_size.height - self.child_size.height
        
        return (x, y)
    

    
