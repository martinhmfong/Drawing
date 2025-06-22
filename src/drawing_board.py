from src.canvas import Canvas
from src.exceptions import CanvasNotReadyError
from src.validators import validate_line_orientation


class DrawingBoard:
    def __init__(self, canvas: Canvas = None):
        self.canvas = canvas

    def __str__(self):
        self._ensure_canvas()
        border = '-' * (self.canvas.width + 2)
        rows = ['|' + ''.join(row) + '|' for row in self.canvas.pixels]
        return '\n'.join([border] + rows + [border])

    def new_canvas(self, width: int, height: int):
        self.canvas = Canvas(width, height)

    def _ensure_canvas(self):
        if not self.canvas:
            raise CanvasNotReadyError('Canvas not ready, please initiate a new canvas')

    def _validate_line(self, x1: int, y1: int, x2: int, y2: int):
        validate_line_orientation(x1, y1, x2, y2)
        for point in ((x1, y1), (x2, y2)):
            self.canvas.valid_point(*point)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, c: str):
        self._ensure_canvas()
        self._validate_line(x1, y1, x2, y2)

        if x1 == x2:  # Vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.canvas.draw_pixel(x1, y, c)
        else:  # Horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.canvas.draw_pixel(x, y1, c)

    def draw_rectangle(self, x1: int, y1: int, x2: int, y2: int, c: str):
        self._ensure_canvas()

        left, right = min(x1, x2), max(x1, x2)
        top, bottom = min(y1, y2), max(y1, y2)

        for point in ((left, top), (right, top), (left, bottom), (right, bottom)):
            self.canvas.valid_point(*point)

        self.draw_line(left, top, right, top, c)
        self.draw_line(left, bottom, right, bottom, c)
        self.draw_line(left, top, left, bottom, c)
        self.draw_line(right, top, right, bottom, c)

    def bucket_fill(self, x: int, y: int, c: str):
        self._ensure_canvas()
        self.canvas.valid_point(x, y)

        start_color = self.canvas.get_pixel(x, y)
        if start_color == c:
            return

        stack = [(x, y)]
        visited = set()

        while stack:
            current_x, current_y = stack.pop()

            if (current_x, current_y) in visited:
                continue

            visited.add((current_x, current_y))

            if not self.canvas.is_inside(current_x, current_y) or \
                    self.canvas.get_pixel(current_x, current_y) != start_color:
                continue

            self.canvas.draw_pixel(current_x, current_y, c)

            neighbors = [
                (current_x + dx, current_y + dy)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                if self.canvas.is_inside(current_x + dx, current_y + dy)
            ]
            stack.extend(n for n in neighbors if n not in visited)
