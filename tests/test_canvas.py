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
        # Valid points (1-based)
        c.draw_pixel(1, 1, 'A')
        self.assertEqual(c.pixels[0][0], 'A')
        c.draw_pixel(3, 3, 'B')
        self.assertEqual(c.pixels[2][2], 'B')

        # Replace the existing pixel
        c.draw_pixel(1, 1, 'X')
        self.assertEqual(c.pixels[0][0], 'X')

    def test_out_of_canvas(self):
        cases = (
            (4, 1,),
            (1, 4,),
            (0, 2,),
            (2, 0,),
            (-1, 2),
            (2, -1),
        )

        c = Canvas(3, 3)
        for x, y in cases:
            with self.assertRaises(OutOfCanvasError):
                c.draw_pixel(x, y, '*')
