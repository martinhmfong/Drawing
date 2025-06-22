from src.exceptions import OutOfCanvasError
from src.validators import validate_dimensions


class Canvas:
    """A 2D canvas for drawing with characters.

    The canvas uses 1-based indexing for x and y coordinates.
    Origin (1,1) is at the top-left corner of the canvas.
    """

    def __init__(self, width: int, height: int):
        validate_dimensions(width, height)
        self.width = width
        self.height = height
        self.pixels = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def is_inside(self, x: int, y: int) -> bool:
        return 0 < x <= self.width and 0 < y <= self.height

    def valid_point(self, x: int, y: int):
        if self.is_inside(x, y):
            return
        raise OutOfCanvasError(f"The required pixel ({x},{y}) is outside of the canvas [{self.width}, {self.height}]")

    def draw_pixel(self, x: int, y: int, char: str):
        self.valid_point(x, y)
        self.pixels[y - 1][x - 1] = char

    def get_pixel(self, x: int, y: int) -> str:
        self.valid_point(x, y)
        return self.pixels[y - 1][x - 1]
