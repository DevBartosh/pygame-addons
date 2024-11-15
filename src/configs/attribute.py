from typing import Any

class Attribute:
    """
    Class representing an attribute in attribute list in `Config` class.
    """
    def __init__(
        self,
        name: str,
        attr_type: type,
        default: Any = None
    ) -> None:
        self.name = name
        self.attr_type = attr_type
        self.default = default

        if default is not None and not isinstance(default, attr_type):
            raise TypeError(
                self.name + " was given a default value of a wrong type."
            )