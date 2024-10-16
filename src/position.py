from align import Align
from surface_aligner import SurfaceAligner

class Position:
    def __init__(self,
                 x: int = 0,
                 y: int = 0,
                 width_perc: float = 0.0,
                 height_perc: float = 0.0,
                 align: Align = Align.TOP_LEFT,
                 surface_aligner: SurfaceAligner | None = None
                 ) -> None:
        self.x = x
        self.y = y
        self.width_perc = width_perc
        self.height_perc = height_perc
        self.align = align
        self.surface_aligner = surface_aligner
        self.generate_position()
    
    def update(self,
                x: int | None = None,
                y: int | None = None,
                width_perc: float | None = None,
                height_perc: float | None = None,
                align: Align | None = None
                ) -> None:
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if width_perc is not None:
            self.width_perc = width_perc
        if height_perc is not None:
            self.height_perc = height_perc
        if align is not None:
            self.align = align
        self.generate_position()

    def generate_position(self) -> None:
        align_x = 0
        align_y = 0
        perc_x = 0
        perc_y = 0

        if self.surface_aligner is not None:
            align_pos = self.surface_aligner.get_align_pos(self.align)
            align_x = align_pos[0]
            align_y = align_pos[1]
            perc_x = int(self.width_perc * self.surface_aligner.parent_size.width)
            perc_y = int(self.height_perc * self.surface_aligner.parent_size.height)

        self.x_pos = self.x + perc_x + align_x
        self.y_pos = self.y + perc_y + align_y

    def get_x(self) -> int:
        return self.x_pos

    def get_y(self) -> int:
        return self.y_pos