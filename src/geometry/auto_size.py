from typing import Self

from ..exceptions import VariableNotImplementedError
from ..utils.represent import get_repr

class AutoSize:
    """
    Class allowing for the use of automatic size setting.\n
    Pass width_auto_setting and height_auto_setting to constructor to control which attributes
    of size should or should not be automatically set. If ..._auto_setting parameter will be true and
    corresponding value was not set, code will return an error.
    """
    def __init__(
        self,
        raw_width: int = 0,
        raw_height: int = 0,
        width_auto_setting: bool = True,
        height_auto_setting: bool = True,
    ) -> None:
        self._raw_width = raw_width
        self._raw_height = raw_height
        self._width_auto_setting = width_auto_setting
        self._height_auto_setting = height_auto_setting
        self._set_width: int | None = None
        self._set_height: int | None = None
    
    @property
    def width(self) -> int:
        total_width = self.raw_width
        if not self.width_auto_setting:
            return total_width
        
        if self.set_width is None:
            raise VariableNotImplementedError(
                    "width_auto_setting is True, but set_width is not set."
                )
        total_width += self.set_width

        return total_width

    @property
    def height(self) -> int:
        total_height = self.raw_height
        if not self.height_auto_setting:
            return total_height
        
        if self.set_height is None:
            raise VariableNotImplementedError(
                "height_auto_setting is True, but set_height is not set."
            )
        total_height += self.set_height

        return total_height
    
    @property
    def raw_width(self) -> int:
        return self._raw_width
    
    @raw_width.setter
    def raw_width(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"raw_width must be of type int, got {type(value).__name__}.")
        if value < 0:
            raise ValueError(f"raw_width cannot be less than 0.")
        self._raw_width = value
        
    @property
    def raw_height(self) -> int:
        return self._raw_height
    
    @raw_height.setter
    def raw_height(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"raw_height must be of type int, got {type(value).__name__}.")
        if value < 0:
            raise ValueError(f"raw_height cannot be less than 0.")
        self._raw_height = value
    
    @property
    def width_auto_setting(self) -> bool:
        return self._width_auto_setting
    
    @width_auto_setting.setter
    def width_auto_setting(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f"width_auto_setting must be of type bool, got {type(value).__name__}")
        self._width_auto_setting = value

    @property
    def height_auto_setting(self) -> bool:
        return self._height_auto_setting
    
    @height_auto_setting.setter
    def height_auto_setting(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f"height_auto_setting must be of type bool, got {type(value).__name__}")
        self._height_auto_setting = value

    @property
    def set_width(self) -> int | None:
        return self._set_width
    
    @set_width.setter
    def set_width(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"set_width must be of type int or None, got {type(value).__name__}.")
        if value < 0:
            raise ValueError(f"set_width cannot be less than 0.")
        self._raw_width = value
    
    @property
    def set_height(self) -> int | None:
        return self._set_height
    
    @set_height.setter
    def set_height(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"set_height must be of type int or None, got {type(value).__name__}.")
        if value < 0:
            raise ValueError(f"set_height cannot be less than 0.")
        self._set_height = value

    def to_tuple(self) -> tuple[int, int]:
        return self.width, self.height
    
    @classmethod
    def from_tuple(cls, size_tuple: tuple[int, int]) -> Self:
        return cls(*size_tuple)
    
    def __str__(self) -> str:
        return get_repr(self)
    
    def __eq__(self, other: object) -> bool:
        return get_repr(self) == get_repr(other)
