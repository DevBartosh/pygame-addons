from geometry.align import Align
from geometry.surface_aligner import SurfaceAligner
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
        aligner: SurfaceAligner | None = None
    ) -> None:
        self.x = x
        self.y = y
        self.width_perc = width_perc
        self.height_perc = height_perc
        self.align = align
        self.surface_aligner = aligner

        aligner_used = width_perc != 0 or height_perc != 0 or align != Align.NONE
        if aligner_used and aligner is None:
            raise VariableNotImplementedError(
                "surface aligner was not initialized for positioning with percents or alignment."
            )

    def get_x(self) -> int:
        perc_x = 0
        align_x = 0
        if self.surface_aligner is not None:
            perc_x = int(self.width_perc * self.surface_aligner.parent_size.width)
            align_x = self.surface_aligner.get_align_pos(self.align)[0]
        return self.x + perc_x + align_x

    def get_y(self) -> int:
        perc_y = 0
        align_y = 0
        if self.surface_aligner is not None:
            perc_y = int(self.height_perc * self.surface_aligner.parent_size.height)
            align_y = self.surface_aligner.get_align_pos(self.align)[1]
        return self.y + perc_y + align_y
    
    def get_tuple(self) -> tuple[int, int]:
        return (self.get_x(), self.get_y())