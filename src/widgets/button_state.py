from enum import StrEnum, auto

class ButtonState(StrEnum):
    REST = "REST"
    PRESS = "PRESS"
    HOVER = "HOVER"
    DISABLE = "DISABLE"