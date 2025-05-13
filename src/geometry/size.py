from typing import Self

class Size:
    """
    Class containing width and height of a surface.
    """
    def __init__(self, width: int, height: int) -> None:
        if width < 0:
            raise ValueError(
                "Given width was not positive."
            )
        if height < 0:
            raise ValueError(
                "Given height was not positive."
            )
        self.width = width
        self.height = height
    
    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height
    
    def get_tuple(self) -> tuple[int, int]:
        return self.get_width(), self.get_height()
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        if self.__dict__ != other.__dict__:
            return False
        return True
    
    def __str__(self) -> str:
        return f"Size({self.get_width()}, {self.get_height()})"
    
    @classmethod
    def from_tuple(cls, size_tuple: tuple[int, int]) -> Self:
        return cls(size_tuple[0], size_tuple[1])