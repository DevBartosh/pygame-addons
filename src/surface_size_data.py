from size import Size
from align import Align

class SurfaceSizeData:
    def __init__(self,
                 parent_surface_size: Size,
                 child_surface_size: Size
                 ) -> None:
        self.parent_size = parent_surface_size
        self.child_size = child_surface_size
    
    def get_centered_x(self, parent_width_overwrite: int | None = None, child_width_overwrite: int | None = None) -> int:
        parent_width = self.parent_size.width
        child_width = self.child_size.width

        if parent_width_overwrite is not None:
            parent_width = parent_width_overwrite
        if child_width_overwrite is not None:
            child_width = child_width_overwrite
        
        return (parent_width - child_width) // 2
    
    def get_centered_y(self, parent_height_overwrite: int | None = None, child_height_overwrite: int | None = None) -> int:
        parent_height = self.parent_size.height
        child_height = self.child_size.height

        if parent_height_overwrite is not None:
            parent_height = parent_height_overwrite
        if child_height_overwrite is not None:
            child_height = child_height_overwrite
        
        return (parent_height - child_height) // 2
    
    def get_align_pos(self, align: Align) -> tuple[int, int]:
        match align:
            case Align.TOP_LEFT | Align.MID_LEFT | Align.BOTTOM_LEFT:
                x = 0
            case Align.TOP_MID | Align.MID | Align.BOTTOM_MID:
                x = self.get_centered_x()
            case Align.TOP_RIGHT | Align.MID_RIGHT | Align.BOTTOM_RIGHT:
                x = self.parent_size.width - self.child_size.width
        
        match align:
            case Align.TOP_LEFT | Align.TOP_MID | Align.TOP_RIGHT:
                y = 0
            case Align.MID_LEFT | Align.MID | Align.MID_RIGHT:
                y = self.get_centered_y()
            case Align.BOTTOM_LEFT | Align.BOTTOM_MID | Align.BOTTOM_RIGHT:
                y = self.parent_size.height - self.child_size.height
        
        return (x, y)
    
    def get_width_percentage(self, width_percent: float) -> int:
        return int(width_percent * self.parent_size.width)
    
    def get_height_percentage(self, height_percent: float) -> int:
        return int(height_percent * self.parent_size.height)
    
