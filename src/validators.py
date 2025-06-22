from src.exceptions import CanvasDimensionError, WrongOrientationError


def validate_dimensions(width: int, height: int):
    if width <= 0 and height <= 0:
        raise CanvasDimensionError(f"Canvas dimensions must be positive integers, but input width: {width}, height: {height}")
    if width <= 0:
        raise CanvasDimensionError(f"Canvas width must be a positive integer, but input width: {width}")
    if height <= 0:
        raise CanvasDimensionError(f"Canvas height must be a positive integer, but input height: {height}")


def validate_line_orientation(x1: int, y1: int, x2: int, y2: int):
    if y1 == y2 or x1 == x2:
        return
    raise WrongOrientationError(f'The line ({x1}, {y1}), ({x2}, {y2}) is not vertical or horizontal')
