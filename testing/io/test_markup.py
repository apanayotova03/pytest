import unittest
from unittest.mock import patch
from _pytest._io.terminalwriter import TerminalWriter

class TestTerminalWriterMarkup(unittest.TestCase):

    def setUp(self):
        self.tw = TerminalWriter()

    def test_markup_known_key_non_empty_esc(self):
        print("Testing markup with known markup key and esc list non-empty:")
        result = self.tw.markup("Test", bold=True)
        expected_esc_sequence = "\x1b[1mTest\x1b[0m"
        branches_taken = self.tw.report_markup_branch_usage()
        
        self.assertEqual(result, expected_esc_sequence)
        self.assertEqual(branches_taken, [0, 1, 1, 1, 0, 0])

    def test_markup_known_key_empty_esc(self):
        print("Testing markup with known markup key and esc list empty:")
        result = self.tw.markup("Test", bold=False)
        branches_taken = self.tw.report_markup_branch_usage()
        
        self.assertEqual(result, "Test")
        self.assertEqual(branches_taken, [0, 1, 1, 0, 1, 0])

    def test_markup_unknown_key(self):
        print("Testing markup with unknown markup key:")
        result = self.tw.markup("Test", wrongkey=True)
        branches_taken = self.tw.report_markup_branch_usage()
        
        self.assertEqual(result, "Error: unknown markup: 'wrongkey'")
        self.assertEqual(branches_taken, [1, 0, 0, 0, 0, 0])

    def test_markup_hasmarkup_false(self):
        print("Testing markup with hasmarkup set to False:")
        self.tw.hasmarkup = False
        result = self.tw.markup("Test", bold=True)
        branches_taken = self.tw.report_markup_branch_usage()
        
        self.assertEqual(result, "Test")
        self.assertEqual(branches_taken, [0, 1, 0, 0, 0, 1])

if __name__ == "__main__":
    unittest.main()
