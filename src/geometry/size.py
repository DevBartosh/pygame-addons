from typing import Self

class Size:
    """
    Class containing width and height of a surface.
    """
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def get_tuple(self) -> tuple[int, int]:
        return (self.width, self.height)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        if self.__dict__ != other.__dict__:
            return False
        return True
    
    @classmethod
    def from_tuple(cls, size_tuple: tuple[int, int]) -> Self:
        return cls(size_tuple[0], size_tuple[1])