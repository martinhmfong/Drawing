from unittest import TestCase

from src.drawing_board import DrawingBoard, validate_line_orientation
from src.exceptions import CanvasNotReadyError, WrongOrientationError


class TestDrawingBoard(TestCase):
    def test_new_canvas(self):
        board = DrawingBoard()
        board.new_canvas(3, 4)
        self.assertEqual(board.canvas.width, 3)
        self.assertEqual(board.canvas.height, 4)

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
        board = DrawingBoard()
        board.new_canvas(3, 3)
        board.draw_line(2, 2, 3, 2, '.')
        expected = ('-----\n'
                    '|   |\n'
                    '| ..|\n'
                    '|   |\n'
                    '-----')
        self.assertEqual(str(board), expected)

    def test_draw_line_vertical_visual(self):
        board = DrawingBoard()
        board.new_canvas(5, 5)
        board.draw_line(2, 1, 2, 3, 'y')
        expected = (
            '-------\n'
            '| y   |\n'
            '| y   |\n'
            '| y   |\n'
            '|     |\n'
            '|     |\n'
            '-------'
        )
        self.assertEqual(str(board), expected)

    def test_draw_rectangle_basic(self):
        board = DrawingBoard()
        board.new_canvas(5, 5)
        board.draw_rectangle(2, 2, 4, 4, 'o')
        expected = (
            '-------\n'
            '|     |\n'
            '| ooo |\n'
            '| o o |\n'
            '| ooo |\n'
            '|     |\n'
            '-------'
        )
        self.assertEqual(str(board), expected)

    def test_draw_rectangle_full_canvas(self):
        board = DrawingBoard()
        board.new_canvas(3, 3)
        board.draw_rectangle(1, 1, 3, 3, '*')
        expected = (
            '-----\n'
            '|***|\n'
            '|* *|\n'
            '|***|\n'
            '-----'
        )
        self.assertEqual(str(board), expected)

    def test_draw_rectangle_single_point(self):
        board = DrawingBoard()
        board.new_canvas(4, 4)
        board.draw_rectangle(2, 2, 2, 2, '#')
        expected = (
            '------\n'
            '|    |\n'
            '| #  |\n'
            '|    |\n'
            '|    |\n'
            '------'
        )
        self.assertEqual(str(board), expected)

    def test_draw_rectangle_invalid(self):
        board = DrawingBoard()
        board.new_canvas(3, 3)
        with self.assertRaises(Exception):
            board.draw_rectangle(0, 0, 2, 2, 'x')
        with self.assertRaises(Exception):
            board.draw_rectangle(1, 1, 4, 4, 'x')
