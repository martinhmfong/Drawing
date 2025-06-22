import unittest
from unittest.mock import patch

from runner import main
from runner import validate_params
from src.exceptions import CommandError


class TestRunner(unittest.TestCase):
    def test_validate_params_quit_command(self):
        """Test validation of quit command."""
        self.assertEqual(validate_params('Q', []), ())

    def test_validate_params_canvas_command(self):
        """Test validation of canvas command."""
        self.assertEqual(validate_params('C', ['10', '20']), (10, 20))

    def test_validate_params_line_command(self):
        """Test validation of line command."""
        self.assertEqual(validate_params('L', ['1', '2', '3', '4', 'x']), (1, 2, 3, 4, 'x'))

    def test_validate_params_rectangle_command(self):
        """Test validation of rectangle command."""
        self.assertEqual(validate_params('R', ['1', '2', '3', '4', 'x']), (1, 2, 3, 4, 'x'))

    def test_validate_params_bucket_fill_command(self):
        """Test validation of bucket fill command."""
        self.assertEqual(validate_params('B', ['1', '2', 'o']), (1, 2, 'o'))

    def test_validate_params_invalid_canvas_dimensions(self):
        """Test validation with invalid canvas dimensions."""
        with self.assertRaisesRegex(CommandError, "Canvas dimensions must be integers"):
            validate_params('C', ['abc', 'def'])

    def test_validate_params_invalid_coordinates(self):
        """Test validation with invalid coordinates."""
        with self.assertRaisesRegex(CommandError, "Coordinates must be integers"):
            validate_params('L', ['abc', '1', '2', '3', 'x'])

    def test_validate_params_missing_parameters_line(self):
        """Test validation with missing parameters for line command."""
        with self.assertRaisesRegex(CommandError, "L requires 5 parameters: x1 y1 x2 y2 c"):
            validate_params('L', ['1', '2', '3'])

    def test_validate_params_missing_parameters_rectangle(self):
        """Test validation with missing parameters for rectangle command."""
        with self.assertRaisesRegex(CommandError, "R requires 5 parameters: x1 y1 x2 y2 c"):
            validate_params('R', ['1', '2', '3'])

    def test_validate_params_missing_parameters_bucket(self):
        """Test validation with missing parameters for bucket fill command."""
        with self.assertRaisesRegex(CommandError, "B requires 3 parameters: x y c"):
            validate_params('B', ['1'])

    def test_validate_params_unknown_command(self):
        """Test validation with unknown command."""
        with self.assertRaisesRegex(CommandError, "Unknown command: X"):
            validate_params('X', [])

    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_quit_command(self, mock_print, mock_input):
        """Test main program flow with quit command."""
        mock_input.return_value = 'Q'
        main()
        mock_print.assert_any_call('Quitting...')

    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_empty_command(self, mock_print, mock_input):
        """Test main program flow with empty command."""
        mock_input.side_effect = ['', 'Q']
        main()
        mock_print.assert_any_call('Quitting...')

    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_invalid_command(self, mock_print, mock_input):
        """Test main program flow with invalid command."""
        mock_input.side_effect = ['X', 'Q']
        main()
        mock_print.assert_any_call('Command error: Unknown command: X')

    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_draw_without_canvas(self, mock_print, mock_input):
        mock_input.side_effect = ['L 1 2 3 4 x', 'Q']
        main()
        error_found = False
        for call in mock_print.call_args_list:
            if len(call.args) > 0:
                msg = call.args[0]
                if isinstance(msg, str) and "Canvas not ready" in msg:
                    error_found = True
                    break
        self.assertTrue(error_found, "Canvas not ready error message not found")

    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_successful_canvas_creation(self, mock_print, mock_input):
        mock_input.side_effect = ['C 10 10', 'L 5 7 8 7 +', 'Q']
        main()
        any_error = False
        for call in mock_print.call_args_list:
            if len(call.args) > 0:
                output = call.args[0]
                if isinstance(output, str) and 'error' in output:
                    any_error = True
                    break
        self.assertFalse(any_error, "Error Found")
