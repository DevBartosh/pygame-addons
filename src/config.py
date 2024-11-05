from typing import Self
from copy import copy

from attribute import Attribute
from exceptions.variable_not_implemented import VariableNotImplementedError

class Config:
    attributes: list[Attribute]
    
    def __init__(self, **kwargs) -> None:
        self.modify(**kwargs)

    def modify(self, attr_safe=True, **kwargs) -> None:
        attr_names = [attr.name for attr in self.attributes]

        for key in kwargs.keys():
            if key not in attr_names and attr_safe:
                raise AttributeError(f"Attribute {key} is not recognized.")
        
        for attribute in self.attributes:
            value = kwargs.get(attribute.name, attribute.default)

            if value is None and attr_safe:
                raise VariableNotImplementedError(
                    f"Argument {attribute.name} was not passed for config modification and does not have a default value."
                )
            if not isinstance(value, attribute.attr_type) and attr_safe:
                raise TypeError(f"Attribute {key} has a value of a wrong type.")

            setattr(self, attribute.name, value)
            
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
