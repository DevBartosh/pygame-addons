from typing import Self
from copy import copy

class Config:
    attributes_and_types: dict = {}
    
    def __init__(self, **kwargs) -> None:
        self.modify(**kwargs)

    def modify(self, attr_safe=True, **kwargs) -> None:
        for key, value in kwargs.items():
            if attr_safe:
                if key not in self.attributes_and_types:
                    raise AttributeError(f"Attribute {key} is not recognized.")
                if not isinstance(value, self.attributes_and_types[key]):
                    raise TypeError(f"Attribute {key} has a value of a wrong type.")
            
            setattr(self, key, value)
    
    def get_modified(self, **kwargs) -> Self:
        new = copy(self)
        new.modify(**kwargs)
        return new
    
    def __str__(self) -> str:
        string = f"""
        {self.__class__.__name__} (
        {(",\n\t".join(list(f"{attr}: {self.__dict__[attr]}" for attr in self.__dict__)))}
        )
        """
        return string
