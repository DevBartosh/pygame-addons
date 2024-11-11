from align import Align
from surface_aligner import SurfaceAligner
from exceptions.variable_not_implemented import VariableNotImplementedError

class Position:
    """
    A class containing Position of a widget.

    This class has multiple ways of handling position.
    1. x, y - classic integer values.
    2. width_perc, height_perc - these represent percents of parent surface size (most of the time it is window). 1*
    3. align - represents basic alignment in parent surface. 2*

    1* - parameter needs surface aligner with parent surface size.
    2* - parameter needs surface aligner with both parent and child surface sizes.  

    """
    def __init__(self,
        x: int = 0,
        y: int = 0,
        width_perc: float = 0.0,
        height_perc: float = 0.0,
        align: Align = Align.NONE,
        surface_aligner: SurfaceAligner | None = None
    ) -> None:
        self.x = x
        self.y = y
        self.width_perc = width_perc
        self.height_perc = height_perc
        self.align = align
        self.surface_aligner = surface_aligner
        self.generate_position()

        aligner_used = width_perc != 0 or height_perc != 0 or align != Align.NONE
        if aligner_used and surface_aligner is None:
            raise VariableNotImplementedError(
                "surface_aligner was not initialized for positioning with percents or alignment."
            )
    
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
    
    def get_tuple(self) -> tuple[int, int]:
        return (self.x_pos, self.y_pos)