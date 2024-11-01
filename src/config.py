from typing import Self
from copy import copy

class Config:
    allowed_attributes: dict = {}
    
    def __init__(self, **kwargs) -> None:
        self.modify(**kwargs)

    def modify(self, attr_safe=True, **kwargs) -> None:
        for key, value in kwargs.items():
            if attr_safe:
                if key not in self.allowed_attributes:
                    raise AttributeError(f"Attribute {key} is not recognized.")
                if not isinstance(value, self.allowed_attributes[key]):
                    raise TypeError(f"Attribute {key} has a value of a wrong type.")
            
            setattr(self, key, value)
    
    def get_modified(self, **kwargs) -> Self:
        new = copy(self)
        new.modify(**kwargs)
        return new
    
    def __str__(self) -> str:
        string = f"{self.__class__.__name__} ("
        for key, value in self.__dict__.items():
            string += f"\n\t{key}: {value},"
        string += "\n)"

        return string
