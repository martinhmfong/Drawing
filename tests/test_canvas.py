from unittest import TestCase

from src.canvas import Canvas
from src.exceptions import CanvasDimensionError, OutOfCanvasError


class TestCanvas(TestCase):
    def test_validate_canvas(self):
        # Valid dimensions
        c = Canvas(5, 3)
        self.assertEqual(c.width, 5)
        self.assertEqual(c.height, 3)

        # Invalid width
        with self.assertRaises(CanvasDimensionError):
            Canvas(0, 3)

        # Invalid height
        with self.assertRaises(CanvasDimensionError):
            Canvas(5, 0)

        # Both invalid
        with self.assertRaises(CanvasDimensionError):
            Canvas(0, 0)

    def test_draw_point(self):
        c = Canvas(3, 3)
        c.draw_pixel(1, 1, 'A')
        self.assertEqual(c.pixels[1][1], 'A')

        # Replace the exiting pixel
        c.draw_pixel(1, 1, 'X')
        self.assertEqual(c.pixels[1][1], 'X')

        # Out of bounds
        with self.assertRaises(OutOfCanvasError):
            c.draw_pixel(4, 1, 'B')

        with self.assertRaises(OutOfCanvasError):
            c.draw_pixel(-1, 2, 'C')
