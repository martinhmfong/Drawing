from unittest import TestCase

from src.exceptions import CanvasDimensionError, WrongOrientationError
from src.validators import validate_dimensions, validate_line_orientation


class TestValidators(TestCase):
    def test_validate_dimensions(self):
        validate_dimensions(1, 1)
        validate_dimensions(100, 50)
        validate_dimensions(1000, 1000)

        # Invalid cases
        with self.assertRaises(CanvasDimensionError):
            validate_dimensions(0, 5)
        with self.assertRaises(CanvasDimensionError):
            validate_dimensions(5, 0)
        with self.assertRaises(CanvasDimensionError):
            validate_dimensions(0, 0)
        with self.assertRaises(CanvasDimensionError):
            validate_dimensions(-1, 5)
        with self.assertRaises(CanvasDimensionError):
            validate_dimensions(5, -1)

    def test_invalidate_dimensions(self):
        invalid_cases = [
            (-1, -1),
            (-1, 0),
            (0, -1),
            (-1, 1),
            (1, -1),
        ]
        for width, height in invalid_cases:
            with self.assertRaises(CanvasDimensionError):
                validate_dimensions(width, height)

    def test_validate_line_orientation(self):
        # Valid horizontal lines
        validate_line_orientation(1, 5, 10, 5)
        validate_line_orientation(10, 5, 1, 5)
        validate_line_orientation(1, 1, 1, 1)

        # Valid vertical lines
        validate_line_orientation(5, 1, 5, 10)
        validate_line_orientation(5, 10, 5, 1)

    def test_invalidate_line_orientation(self):
        # Invalid diagonal lines
        with self.assertRaises(WrongOrientationError):
            validate_line_orientation(1, 1, 2, 2)
        with self.assertRaises(WrongOrientationError):
            validate_line_orientation(1, 2, 2, 3)
        with self.assertRaises(WrongOrientationError):
            validate_line_orientation(2, 2, 1, 1)
