from src.exceptions import CanvasDimensionError, OutOfCanvasError


class Canvas:
    """Simple canvas to persist pixels with a method to draw a point."""

    def __init__(self, width: int, height: int):
        self._validate_dimensions(width, height)
        self.width = width
        self.height = height
        self.pixels = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.pixels)

    @staticmethod
    def _validate_dimensions(width, height):
        if width <= 0 and height <= 0:
            raise CanvasDimensionError(f"Canvas dimensions must be positive integers, but input width: {width}, height: {height}")
        if width <= 0:
            raise CanvasDimensionError(f"Canvas width must be a positive integer, but input width: {width}")
        if height <= 0:
            raise CanvasDimensionError(f"Canvas height must be a positive integer, but input height: {height}")

    def is_valid_point(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def draw_pixel(self, x: int, y: int, char: str):
        """
        Draw a character at the specified (x, y) position.
        Character validation should be handled at the command level before drawing on the board.
        """
        if not self.is_valid_point(x, y):
            raise OutOfCanvasError(f"The required pixel ({x},{y}) is outside of the canvas [{self.width}, {self.height}]")
        self.pixels[y][x] = char
