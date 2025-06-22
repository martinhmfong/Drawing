from unittest import TestCase

from src.drawing_board import DrawingBoard, validate_line_orientation
from src.exceptions import CanvasNotReadyError, WrongOrientationError


class TestDrawingBoard(TestCase):
    def setUp(self):
        self.board = DrawingBoard()
        self.board.new_canvas(5, 5)

    def test_new_canvas(self):
        self.board.new_canvas(3, 4)
        self.assertEqual(self.board.canvas.width, 3)
        self.assertEqual(self.board.canvas.height, 4)

    def test_validate_line_orientation(self):
        # Valid horizontal
        validate_line_orientation(1, 2, 3, 2)
        # Valid vertical
        validate_line_orientation(2, 1, 2, 4)
        # Invalid
        with self.assertRaises(WrongOrientationError):
            validate_line_orientation(1, 1, 2, 2)

    def test_draw_line_no_canvas(self):
        board = DrawingBoard()
        with self.assertRaises(CanvasNotReadyError):
            board.draw_line(1, 1, 1, 2, 'x')

    def test_draw_line_horizontal_visual(self):
        self.board.draw_line(2, 2, 3, 2, '.')
        expected = (
            '-------\n'
            '|     |\n'
            '| ..  |\n'
            '|     |\n'
            '|     |\n'
            '|     |\n'
            '-------'
        )
        self.assertEqual(str(self.board), expected)

    def test_draw_line_vertical_visual(self):
        self.board.draw_line(2, 1, 2, 3, 'y')
        expected = (
            '-------\n'
            '| y   |\n'
            '| y   |\n'
            '| y   |\n'
            '|     |\n'
            '|     |\n'
            '-------'
        )
        self.assertEqual(str(self.board), expected)
