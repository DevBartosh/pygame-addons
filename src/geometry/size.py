class Size:
    """
    Class containing width and height of a surface.
    """
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def get_tuple(self) -> tuple[int, int]:
        return (self.width, self.height)