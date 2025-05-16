from typing import Self, Any
from collections.abc import Callable
from copy import copy

import pygame

from . import Attribute
from ..exceptions import VariableNotImplementedError
from ..utils.surface import surfaces_equal
from ..utils.represent import get_repr_surface

class Config:
    """
    Base class for configurations.

    While making a subclass, define `attributes` list to control possible parameters.
    This class supports modifying, comparing with == and representing in string.
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
        convert_func: Callable[[Any], str]
        values: list[str] = []

        string = f"{self.__class__.__name__}("
        for key, value in self.__dict__.items():
            if isinstance(value, pygame.Surface):
                convert_func = get_repr_surface
            else:
                convert_func = str

            values.append(f"{key}={convert_func(value)}")
        string += ",".join(values)
        string += ")"

        return string

    def __eq__(self, other: object) -> bool:
        comparing_func: Callable[[Any, Any], bool]
        
        if not isinstance(other, self.__class__):
            return False
        if self.__dict__.keys() != other.__dict__.keys():
            return False
        
        for key in self.__dict__.keys():
            self_value = self.__dict__[key]
            other_value = other.__dict__[key]

            if not isinstance(other_value, type(self_value)):
                return False
            
            if isinstance(self_value, pygame.Surface):
                comparing_func = surfaces_equal
            else:
                comparing_func = lambda x, y: x == y
            
            if not comparing_func(self_value, other_value):
                return False
            
        return True