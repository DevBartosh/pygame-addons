from typing import Self, Any
from copy import copy

from .attribute import Attribute
from ..exceptions.variable_not_implemented import VariableNotImplementedError

class Config:
    """
    Base class for configurations like `Style` and `Content`.

    While making a subclass, define `attributes` list to control possible attributes.
    """
    attributes: list[Attribute]
    
    def __init__(self, **kwargs: Any) -> None:
        self.modify(default_if_not_given=True, **kwargs)

    def modify(
        self,
        **kwargs: Any
    ) -> None:
        default_if_not_given = kwargs.pop("default_if_not_given", False)

        for key in kwargs.keys():
            if key not in [attr.name for attr in self.attributes]:
                raise AttributeError(f"Attribute {key} is not recognized.")

        for attr in self.attributes:
            if attr.name not in kwargs.keys() and default_if_not_given is False:
                continue

            value: Any = kwargs.get(attr.name, attr.default)
            if value is None:
                raise VariableNotImplementedError(
                    f"Attribute {attr.name} was not passed for " \
                    f"config modification and does not have a default value."
                )

            if not isinstance(value, attr.attr_type):
                raise TypeError(
                    f"Attribute {attr.name} with value {value} " \
                    f"should be of type {attr.attr_type.__name__}."
                )
            
            setattr(self, attr.name, value)
            
            
    def get_modified(self, **kwargs: Any) -> Self:
        new = copy(self)
        new.modify(**kwargs)
        return new
    
    def __str__(self) -> str:
        string = f"{self.__class__.__name__} ("
        for key, value in self.__dict__.items():
            string += f"\n\t{key}: {value},"
        string += "\n)"

        return string

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        if self.__dict__ != other.__dict__:
            return False
        return True