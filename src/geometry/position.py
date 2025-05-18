from copy import copy

from . import Align, SurfaceAligner, AutoSize
from ..exceptions import VariableNotImplementedError
from ..utils.represent import get_hash

class Position:
    """
    A class containing and calculating position of a widget.

    This class has multiple ways of handling position.
    Values of the following methods are combined to create final position.
    1. raw_x, raw_y - integer values.
    2. width_percent, height_percent - these represent percents of parent surface size. 1*
    3. align - represents basic alignment in parent surface. 2*

    1* - parameter needs surface aligner with parent surface size.
    2* - parameter needs surface aligner with both parent and child surface sizes.  
    """
    
    def __init__(
        self,
        raw_x: int = 0,
        raw_y: int = 0,
        width_percent: float = 0.0,
        height_percent: float = 0.0,
        align: Align = Align.NONE,
        aligner: SurfaceAligner | None = None
    ) -> None:
        self.raw_x = raw_x
        self.raw_y = raw_y
        self.width_percent = width_percent
        self.height_percent = height_percent
        self.align = align

        self._total_x: int = 0
        self._total_y: int = 0
        self._last_data_hash: str = ""

        if aligner is None:
            self._surface_aligner = None
            aligner_used = (
                width_percent != 0 or 
                height_percent != 0 or 
                align != Align.NONE
            )
            if aligner_used:
                raise VariableNotImplementedError(
                    "Surface aligner was not given for positioning with percents or alignment."
                )
            return None
        
        if isinstance(aligner.child_size, AutoSize):
            self._surface_aligner = copy(aligner)
        else:
            self._surface_aligner = aligner

    @property
    def x(self) -> int:
        data_hash: str = get_hash((
            self.raw_x, self.raw_y,
            self.width_percent, self.height_percent,
            self.align, self.surface_aligner
        ))
        if data_hash != self._last_data_hash:
            self._calculate_x_and_y()
            self._last_data_hash = data_hash
        return self._total_x
    
    @property
    def y(self) -> int:
        data_hash: str = get_hash((
            self.raw_x, self.raw_y,
            self.width_percent, self.height_percent,
            self.align, self.surface_aligner
        ))
        if data_hash != self._last_data_hash:
            self._calculate_x_and_y()
            self._last_data_hash = data_hash
        return self._total_y
    
    @property
    def raw_x(self) -> int:
        return self._raw_x
    
    @raw_x.setter
    def raw_x(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"raw_x must be of type int, got {type(value).__name__}.")
        self._raw_x = value
    
    @property
    def raw_y(self) -> int:
        return self._raw_y
    
    @raw_y.setter
    def raw_y(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"raw_y must be of type int, got {type(value).__name__}.")
        self._raw_y = value

    @property
    def width_percent(self) -> float:
        return self._width_percent
    
    @width_percent.setter
    def width_percent(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError(f"width_percent must be of type float, got {type(value).__name__}.")
        self._width_percent = value

    @property
    def height_percent(self) -> float:
        return self._height_percent
    
    @height_percent.setter
    def height_percent(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError(f"height_percent must be of type float, got {type(value).__name__}.")
        self._height_percent = value

    @property
    def align(self) -> Align:
        return self._align
    @align.setter
    
    def align(self, value: Align) -> None:
        if not isinstance(value, Align):
            raise TypeError(f"align must be of type Align, got {type(value).__name__}.")
        self._align = value

    @property
    def tuple(self) -> tuple[int, int]:
        return self.x, self.y
    
    @property
    def surface_aligner(self) -> SurfaceAligner | None:
        return self._surface_aligner
    
    def _calculate_x_and_y(self) -> None:
        percent_x: int
        percent_y: int
        align_values: tuple[int, int]
        align_x: int
        align_y: int
        aligner_used = (
            self.width_percent != 0 or
            self.height_percent != 0 or
            self.align != Align.NONE
        )

        if self.surface_aligner is None:
            if aligner_used:
                raise VariableNotImplementedError(
                    "Surface aligner was not given for positioning with percents or alignment."
                )
            self._total_x = self.raw_x
            self._total_y = self.raw_y
            return None
        
        align_values = self.surface_aligner.get_align_pos(self.align)
        align_x = align_values[0]
        align_y = align_values[1]
        percent_x = int(self.width_percent * self.surface_aligner.parent_size.get_width())
        percent_y = int(self.height_percent * self.surface_aligner.parent_size.get_height())

        self._total_x = self.raw_x + percent_x + align_x
        self._total_y = self.raw_y + percent_y + align_y
