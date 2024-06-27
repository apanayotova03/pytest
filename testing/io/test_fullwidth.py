from _pytest._io.terminalwriter import TerminalWriter
import unittest
from unittest.mock import patch

class TestTerminalWriter(unittest.TestCase):

    @patch('shutil.get_terminal_size', return_value=(100, 24))
    def test_terminal_writer_no_width_specified(self, mock_get_terminal_size):
        tw = TerminalWriter()
        
        print("Testing with _terminal_width set to None:")
        tw.fullwidth  # Accessing fullwidth to trigger the property
        branch_one, branch_two = tw.report_branch_usage()

        self.assertEqual(branch_one, "Branch 1 was: 0")
        self.assertEqual(branch_two, "Branch 2 was: 0")

    @patch('shutil.get_terminal_size')
    def test_terminal_writer_with_width_specified(self, mock_get_terminal_size):
        mock_get_terminal_size.return_value = (100, 24)
        tw = TerminalWriter()

        print("Testing with _terminal_width set to a specific value (100):")
        tw.fullwidth = 100  # Setting a specific width
        tw.fullwidth  # Accessing fullwidth again to use the setter value
        branch_one, branch_two = tw.report_branch_usage()

        self.assertEqual(branch_one, "Branch 1 was: 0")
        self.assertEqual(branch_two, "Branch 2 was: 0")

if __name__== "_main_":
    unittest.main()
