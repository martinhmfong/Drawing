from src.canvas import Canvas
from src.exceptions import CanvasNotReadyError, WrongOrientationError


def validate_line_orientation(x1: int, y1: int, x2: int, y2: int):
    if y1 == y2 or x1 == x2:
        return
    raise WrongOrientationError(f'The line ({x1}, {y1}), ({x2}, {y2}) is not vertical or horizontal')


class DrawingBoard:
    def __init__(self, canvas: Canvas = None):
        self.canvas = canvas

    def __str__(self):
        border = '-' * (self.canvas.width + 2)
        rows = ['|' + ''.join(row) + '|' for row in self.canvas.pixels]
        return '\n'.join([border] + rows + [border])

    def new_canvas(self, width: int, height: int):
        """Clear and create a new canvas instance."""
        canvas = Canvas(width, height)
        self.canvas = canvas

    def validate_line(self, x1: int, y1: int, x2: int, y2: int):
        validate_line_orientation(x1, y1, x2, y2)
        for point in ((x1, y1), (x2, y2)):
            self.canvas.valid_point(*point)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, c: str):
        if not self.canvas:
            raise CanvasNotReadyError('Canvas not ready, please initiate a new canvas ')
        self.validate_line(x1, y1, x2, y2)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.canvas.draw_pixel(x1, y, c)
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.canvas.draw_pixel(x, y1, c)

    def draw_rectangle(self, x1: int, y1: int, x2: int, y2: int, c: str):
        if not self.canvas:
            raise CanvasNotReadyError('Canvas not ready, please initiate a new canvas ')
        # Ensure top-left and bottom-right order
        left, right = min(x1, x2), max(x1, x2)
        top, bottom = min(y1, y2), max(y1, y2)
        # Validate all four corners (1-based)
        for point in ((left, top), (right, top), (left, bottom), (right, bottom)):
            self.canvas.valid_point(*point)
        # Top and bottom sides
        for x in range(left, right + 1):
            self.canvas.draw_pixel(x, top, c)
            self.canvas.draw_pixel(x, bottom, c)
        # Left and right sides
        for y in range(top + 1, bottom):
            self.canvas.draw_pixel(left, y, c)
            self.canvas.draw_pixel(right, y, c)


if __name__ == '__main__':
    b = DrawingBoard()
    b.new_canvas(10, 10)
    print(b)
    b.draw_line(10, 10, 10, 5, 'x')
    print(b)
    b.draw_rectangle(1, 1, 5, 5, 'y')
    print(b)
    b.draw_rectangle(6, 6, 8, 9, 'z')
    print(b)
