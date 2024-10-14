from align import Align
from surface_size_data import SurfaceSizeData
from size import Size

class Position:
    def __init__(self,
                 x_pos: int = 0,
                 y_pos: int = 0,
                 width_perc: float = 0.0,
                 height_perc: float = 0.0,
                 align: Align = Align.TOP_LEFT,
                 surface_size_data: SurfaceSizeData | None = None
                 ) -> None:
        self.update(x_pos, y_pos, width_perc, height_perc, align, surface_size_data)
    
    def update(self,
                x_pos: int = 0,
                y_pos: int = 0,
                width_perc: float = 0.0,
                height_perc: float = 0.0,
                align: Align = Align.TOP_LEFT,
                surface_size_data: SurfaceSizeData | None = None
                ) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width_perc = width_perc
        self.height_perc = height_perc
        self.align = align
        self.surface_size_data = surface_size_data
        self.generate_position()

    def generate_position(self) -> None:
        if self.surface_size_data is not None:
            align_pos = self.surface_size_data.get_align_pos(self.align)
            align_x = align_pos[0]
            align_y = align_pos[1]
            perc_x = self.surface_size_data.get_width_percentage(self.width_perc)
            perc_y = self.surface_size_data.get_height_percentage(self.height_perc)
        else:
            align_x = 0
            align_y = 0
            perc_x = 0
            perc_y = 0
        self.x = self.x_pos + perc_x + align_x
        self.y = self.y_pos + perc_y + align_y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y