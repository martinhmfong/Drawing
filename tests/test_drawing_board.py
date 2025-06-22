import random
from unittest import TestCase

from src.drawing_board import DrawingBoard
from src.exceptions import CanvasNotReadyError, WrongOrientationError


class TestDrawingBoard(TestCase):

    def test_canvas_management(self):
        board = DrawingBoard()
        board.new_canvas(3, 4)
        self.assertEqual(board.canvas.width, 3)
        self.assertEqual(board.canvas.height, 4)

        board = DrawingBoard()
        with self.assertRaises(CanvasNotReadyError):
            board.draw_line(1, 1, 1, 2, 'x')
        with self.assertRaises(CanvasNotReadyError):
            board.draw_rectangle(1, 1, 2, 2, 'x')
        with self.assertRaises(CanvasNotReadyError):
            board.bucket_fill(1, 1, 'x')

    def test_line_drawing(self):
        board = DrawingBoard()
        board.new_canvas(5, 5)

        board.draw_line(2, 2, 4, 2, '.')
        expected = (
            '-------\n'
            '|     |\n'
            '| ... |\n'
            '|     |\n'
            '|     |\n'
            '|     |\n'
            '-------'
        )
        self.assertEqual(str(board), expected)

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

        with self.assertRaises(WrongOrientationError):
            board.draw_line(1, 1, 2, 2, 'x')

    def test_rectangle_drawing(self):
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

    def test_bucket_fill(self):
        board = DrawingBoard()
        board.new_canvas(3, 3)
        board.bucket_fill(2, 2, '*')
        expected = (
            '-----\n'
            '|***|\n'
            '|***|\n'
            '|***|\n'
            '-----'
        )
        self.assertEqual(str(board), expected)

        board = DrawingBoard()
        board.new_canvas(5, 5)
        board.draw_rectangle(2, 2, 4, 4, 'o')
        board.bucket_fill(3, 3, '*')
        expected = (
            '-------\n'
            '|     |\n'
            '| ooo |\n'
            '| o*o |\n'
            '| ooo |\n'
            '|     |\n'
            '-------'
        )
        self.assertEqual(str(board), expected)

        board = DrawingBoard()
        board.new_canvas(5, 5)
        board.draw_rectangle(2, 2, 4, 4, 'o')
        board.bucket_fill(1, 1, '#')
        expected = (
            '-------\n'
            '|#####|\n'
            '|#ooo#|\n'
            '|#o o#|\n'
            '|#ooo#|\n'
            '|#####|\n'
            '-------'
        )
        self.assertEqual(str(board), expected)

        board = DrawingBoard()
        board.new_canvas(3, 3)
        board.bucket_fill(1, 1, ' ')
        expected = '-----\n|   |\n|   |\n|   |\n-----'
        self.assertEqual(str(board), expected)

    def test_bucket_fill_edge_cases(self):
        board = DrawingBoard()
        board.new_canvas(3, 3)
        board.bucket_fill(1, 1, '*')
        expected = (
            '-----\n'
            '|***|\n'
            '|***|\n'
            '|***|\n'
            '-----'
        )
        self.assertEqual(str(board), expected)

        board = DrawingBoard()
        board.new_canvas(5, 5)
        board.draw_rectangle(2, 2, 4, 4, 'o')
        board.canvas.draw_pixel(3, 3, ' ')
        board.bucket_fill(3, 3, '*')
        expected = (
            '-------\n'
            '|     |\n'
            '| ooo |\n'
            '| o*o |\n'
            '| ooo |\n'
            '|     |\n'
            '-------'
        )
        self.assertEqual(str(board), expected)

        board = DrawingBoard()
        board.new_canvas(4, 4)
        for i in range(1, 5):
            board.canvas.draw_pixel(i, 1, 'x')
            board.canvas.draw_pixel(i, 4, 'x')
            board.canvas.draw_pixel(1, i, 'x')
            board.canvas.draw_pixel(4, i, 'x')
        board.bucket_fill(2, 2, '#')
        expected = (
            '------\n'
            '|xxxx|\n'
            '|x##x|\n'
            '|x##x|\n'
            '|xxxx|\n'
            '------'
        )
        self.assertEqual(str(board), expected)

    def test_complex_drawing_combinations(self):
        board = DrawingBoard()
        board.new_canvas(7, 7)
        board.draw_rectangle(1, 1, 7, 7, '*')
        board.draw_rectangle(3, 3, 5, 5, 'o')
        board.bucket_fill(2, 2, '#')
        expected = (
            '---------\n'
            '|*******|\n'
            '|*#####*|\n'
            '|*#ooo#*|\n'
            '|*#o o#*|\n'
            '|*#ooo#*|\n'
            '|*#####*|\n'
            '|*******|\n'
            '---------'
        )
        self.assertEqual(str(board), expected)

        board = DrawingBoard()
        board.new_canvas(5, 5)
        board.draw_line(1, 3, 4, 3, 'x')
        board.draw_line(3, 1, 3, 5, 'x')
        board.bucket_fill(1, 1, '#')
        expected = (
            '-------\n'
            '|##x  |\n'
            '|##x  |\n'
            '|xxxx |\n'
            '|  x  |\n'
            '|  x  |\n'
            '-------'
        )
        self.assertEqual(str(board), expected)

    def test_ultra_large_bucket_fill(self):
        board = DrawingBoard()

        size = 1000
        board.new_canvas(size, size)
        board.draw_rectangle(1, 1, size, size, '#')
        board.bucket_fill(2, 2, '*')

        # Verify the fill worked correctly by checking corners and some random points
        self.assertEqual(board.canvas.get_pixel(1, 1), '#')
        self.assertEqual(board.canvas.get_pixel(size, 1), '#')
        self.assertEqual(board.canvas.get_pixel(1, size), '#')
        self.assertEqual(board.canvas.get_pixel(size, size), '#')

        # Check some interior points
        interior_points = [
            (random.randint(2, size - 1), random.randint(2, size - 1))
            for _ in range(50)
        ]
        for x, y in interior_points:
            self.assertEqual(
                board.canvas.get_pixel(x, y), '*',
                f"Interior point ({x},{y}) should be filled with '*'"
            )
