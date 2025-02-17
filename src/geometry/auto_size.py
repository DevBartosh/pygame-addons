from ..exceptions import VariableNotImplementedError

class AutoSize:
    """
    Class allowing for the use of automatic size setting.\n
    Pass auto_width and auto_height to constructor to control which attributes
    of size should or should not be automatically set. If auto_[...] parameter will be true and
    corresponding value was not set, code will return an error.
    """
    def __init__(
        self,
        width: int = 0,
        height: int = 0,
        auto_width: bool = True,
        auto_height: bool = True,
    ) -> None:
        if width < 0:
            raise ValueError(
                "Given width was negative."
            )
        if height < 0:
            raise ValueError(
                "Given height was negative."
            )
        self.width = width
        self.height = height
        self.auto_width = auto_width
        self.auto_height = auto_height
        self.set_width: int | None = None
        self.set_height: int | None = None
    
    def get_width(self) -> int:
        total_width = 0
        total_width += self.width
        if self.auto_width:
            if self.set_width is None:
                raise VariableNotImplementedError(
                    "Width was declared auto but was not set in AutoSize instance."
                )
            total_width += self.set_width

        return total_width

    def get_height(self) -> int:
        total_height = 0
        total_height += self.height
        if self.auto_height:
            if self.set_height is None:
                raise VariableNotImplementedError(
                    "Height was declared auto but was not set in AutoSize instance."
                )
            total_height += self.set_height

        return total_height
    
    def get_tuple(self) -> tuple[int, int]:
        return self.get_width(), self.get_height()
    
    def __str__(self) -> str:
        return f"AutoSize({self.get_width()}, {self.get_height()})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        if self.__dict__ != other.__dict__:
            return False
        return True
