from copy import copy

from . import Align, SurfaceAligner, AutoSize
from ..exceptions import VariableNotImplementedError

class Position:
    """
    A class containing and calculating position of a widget.

    This class has multiple ways of handling position.
    1. x, y - integer values.
    2. width_perc, height_perc - these represent percents of parent surface size. 1*
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

        if aligner is None:
            self.surface_aligner = None
            aligner_used = (
                width_perc != 0 or 
                height_perc != 0 or 
                align != Align.NONE
            )
            if aligner_used:
                raise VariableNotImplementedError(
                    "Surface aligner was not given for positioning with percents or alignment."
                )
            return
        
        if isinstance(aligner.child_size, AutoSize):
            self.surface_aligner = copy(aligner)
        else:
            self.surface_aligner = aligner

    def get_x(self) -> int:
        perc_x: int
        align_x: int
        aligner_used = (
            self.width_perc != 0 or 
            self.height_perc != 0 or 
            self.align != Align.NONE
        )
        if self.surface_aligner is None:
            if aligner_used:
                raise VariableNotImplementedError(
                    "Surface aligner was not given for positioning with percents or alignment."
                )
            return self.x
        perc_x = int(
            self.width_perc *
            self.surface_aligner.parent_size.get_width()
        )
        align_x = self.surface_aligner.get_align_pos(self.align)[0]
        
        return self.x + perc_x + align_x

    def get_y(self) -> int:
        perc_y: int
        align_y: int
        aligner_used = (
            self.width_perc != 0 or 
            self.height_perc != 0 or 
            self.align != Align.NONE
        )
        if self.surface_aligner is None:
            if aligner_used:
                raise VariableNotImplementedError(
                    "Surface aligner was not given for positioning with percents or alignment."
                )
            return self.y
        
        perc_y = int(
            self.height_perc *
            self.surface_aligner.parent_size.get_height()
        )
        align_y = self.surface_aligner.get_align_pos(self.align)[1]

        return self.y + perc_y + align_y
    
    def get_tuple(self) -> tuple[int, int]:
        return self.get_x(), self.get_y()
