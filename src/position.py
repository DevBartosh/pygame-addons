from typing import Self

from side import Side
from size import Size
from exceptions.variable_not_implemented import VariableNotImplementedError

class Position:
    parent_surface_size: Size | None = None

    def __init__(self: Self,
                 x: int = 0,
                 y: int = 0,
                 width_perc: float = 0,
                 height_perc: float = 0,
                 side: Side | None = None,
                 surface_size: Size | None = None
                 ) -> None:
        self.x = x
        self.y = y
        self.width_perc = width_perc
        self.height_perc = height_perc
        self.side = side
        self.surface_size = surface_size

    def get_x(self):
        return self.x + self.get_percent_x() + self.get_side_x()

    def get_y(self):
        return self.x + self.get_percent_y() + self.get_side_y()
    
    def get_percent_x(self):
        if self.parent_surface_size is None:
            raise VariableNotImplementedError("Position.parent_surface_size is not implemented.")
        
        return self.width_perc * self.parent_surface_size.width
    
    def get_percent_y(self):
        if self.parent_surface_size is None:
            raise VariableNotImplementedError("Position.parent_surface_size is not implemented.")
        
        return self.height_perc * self.parent_surface_size.height
    
    def get_side_x(self: Self) -> int:
        if self.parent_surface_size is None:
            raise VariableNotImplementedError("Position.parent_surface_size is not implemented")
        if self.surface_size is None:
            raise VariableNotImplementedError("self.surface_size is not implemented.")

        x = 0
        match self.side:
            case Side.TOP_LEFT | Side.MID_LEFT | Side.BOTTOM_LEFT:
                x = 0
            case Side.TOP_MID | Side.MID | Side.BOTTOM_MID:
                x = Position.center_x(self.surface_size.width)
            case Side.TOP_RIGHT | Side.MID_RIGHT | Side.BOTTOM_RIGHT:
                x = self.parent_surface_size.width - self.surface_size.width
        
        return x
        
    def get_side_y(self: Self) -> int:
        if self.parent_surface_size is None:
            raise VariableNotImplementedError("Position.parent_surface_size is not implemented.")
        if self.surface_size is None:
            raise VariableNotImplementedError("self.surface_size is not implemented.")

        y = 0
        match self.side:
            case Side.TOP_LEFT | Side.TOP_MID | Side.TOP_RIGHT:
                y = 0
            case Side.MID_LEFT | Side.MID | Side.MID_RIGHT:
                y = Position.center_y(self.surface_size.height)
            case Side.BOTTOM_LEFT | Side.BOTTOM_MID | Side.BOTTOM_RIGHT:
                y = self.parent_surface_size.height - self.surface_size.height

        return y

    @classmethod
    def center_x(cls, surface_width) -> int:
        return cls.parent_surface_size.width / 2 - surface_width / 2
    
    @classmethod
    def center_y(cls, surface_height) -> int:
        return cls.parent_surface_size.height / 2 - surface_height / 2