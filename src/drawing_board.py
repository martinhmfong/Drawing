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


if __name__ == '__main__':
    b = DrawingBoard()
    b.new_canvas(3, 3)
    print(b)
    b.draw_line(2, 2, 3, 2, '.')
    # b.draw_line(2, 4, 4, 4, 'y')
    print(b)
