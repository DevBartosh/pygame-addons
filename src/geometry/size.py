from typing import Self

from ..utils.represent import get_repr

class Size:
    """
    Class containing width and height of a surface.\n
    If negative values are passed into constructor, an error is raised.
    This class supports comparing with ==.
    """
    
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"width must be of type int, got {type(value).__name__}.")
        if value < 0:
            raise ValueError(f"width cannot be less than 0.")
        self._width = value
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"height must be of type int, got {type(value).__name__}.")
        if value < 0:
            raise ValueError(f"height cannot be less than 0.")
        self._height = value
    
    def to_tuple(self) -> tuple[int, int]:
        return self.width, self.height
    
    @classmethod
    def from_tuple(cls, size_tuple: tuple[int, int]) -> Self:
        return cls(*size_tuple)
    
    def __eq__(self, other: object) -> bool:
        return get_repr(self) == get_repr(other)
    
    def __str__(self) -> str:
        return get_repr(self)
