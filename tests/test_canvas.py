from unittest import TestCase

from src.canvas import Canvas
from src.exceptions import CanvasDimensionError, OutOfCanvasError


class TestCanvas(TestCase):

    def test_canvas_initialization(self):
        c = Canvas(5, 3)
        self.assertEqual(c.width, 5)
        self.assertEqual(c.height, 3)
        self.assertEqual(len(c.pixels), 3)
        self.assertEqual(len(c.pixels[0]), 5)

        invalid_dims = [(0, 3), (5, 0), (0, 0), (-1, 3), (3, -1)]
        for width, height in invalid_dims:
            with self.assertRaises(CanvasDimensionError):
                Canvas(width, height)

    def test_is_inside(self):
        canvas = Canvas(3, 3)

        valid_points = [(1, 1), (1, 3), (3, 1), (3, 3), (2, 2)]
        for x, y in valid_points:
            self.assertTrue(canvas.is_inside(x, y))

        invalid_points = [(0, 1), (1, 0), (4, 1), (1, 4), (-1, 1), (1, -1)]
        for x, y in invalid_points:
            self.assertFalse(canvas.is_inside(x, y))

    def test_draw_and_get_pixel(self):
        canvas = Canvas(3, 3)

        self.assertEqual(canvas.get_pixel(1, 1), ' ')

        test_cases = [
            (1, 1, 'A'),
            (3, 3, 'B'),
            (2, 2, 'C')
        ]

        for x, y, char in test_cases:
            canvas.draw_pixel(x, y, char)
            self.assertEqual(canvas.get_pixel(x, y), char)

        canvas.draw_pixel(1, 1, 'X')
        self.assertEqual(canvas.get_pixel(1, 1), 'X')

    def test_out_of_bounds_operations(self):
        canvas = Canvas(3, 3)

        out_of_bounds = [
            (0, 1), (1, 0), (4, 1),
            (1, 4), (-1, 2), (2, -1)
        ]

        for x, y in out_of_bounds:
            with self.assertRaises(OutOfCanvasError):
                canvas.draw_pixel(x, y, '*')
            with self.assertRaises(OutOfCanvasError):
                canvas.get_pixel(x, y)
