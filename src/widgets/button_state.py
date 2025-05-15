from enum import StrEnum

class ButtonState(StrEnum):
    """
    Enum representing possible states of a button.
    """
    REST = "REST"
    PRESS = "PRESS"
    HOVER = "HOVER"
    DISABLE = "DISABLE"