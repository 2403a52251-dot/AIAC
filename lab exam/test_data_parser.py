"""Unit tests for the data_parser module.

Tests the parse_numbers_from_file() and calculate_sum() functions
with various edge cases and malformed input scenarios.

Run with: python -m unittest test_data_parser.py -v
"""

import unittest
import tempfile
import os
from data_parser import parse_numbers_from_file, calculate_sum


class TestDataParser(unittest.TestCase):
    """Unit tests for the data_parser module."""

    def setUp(self):
        """Create temporary directory and files for testing."""
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up temporary files and directories."""
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def _create_test_file(self, content: str) -> str:
        """Helper to create a temporary test file with given content."""
        filepath = os.path.join(self.test_dir, "test_data.txt")
        with open(filepath, 'w') as f:
            f.write(content)
        return filepath

    def test_parse_well_formatted(self):
        """Test parsing well-formatted CSV with no extra spaces."""
        print("Starting: test_parse_well_formatted")
        filepath = self._create_test_file("1,2,3,4,5")
        numbers = parse_numbers_from_file(filepath)
        self.assertEqual(numbers, [1, 2, 3, 4, 5])

    def test_parse_with_extra_spaces(self):
        """Test parsing CSV with extra spaces around numbers."""
        print("Starting: test_parse_with_extra_spaces")
        filepath = self._create_test_file(" 1 , 2 , 3 ")
        numbers = parse_numbers_from_file(filepath)
        self.assertEqual(numbers, [1, 2, 3])

    def test_parse_with_empty_entries(self):
        """Test parsing CSV with empty entries (double commas)."""
        print("Starting: test_parse_with_empty_entries")
        filepath = self._create_test_file("1,,2,,,3")
        numbers = parse_numbers_from_file(filepath)
        self.assertEqual(numbers, [1, 2, 3])

    def test_parse_mixed_formatting(self):
        """Test parsing poorly formatted CSV (from the scenario)."""
        print("Starting: test_parse_mixed_formatting")
        filepath = self._create_test_file("1, 2,3 ,4,,5")
        numbers = parse_numbers_from_file(filepath)
        self.assertEqual(numbers, [1, 2, 3, 4, 5])

    def test_parse_multiline(self):
        """Test parsing multi-line CSV file."""
        print("Starting: test_parse_multiline")
        content = "1, 2\n3 , 4\n5,6"
        filepath = self._create_test_file(content)
        numbers = parse_numbers_from_file(filepath)
        self.assertEqual(numbers, [1, 2, 3, 4, 5, 6])

    def test_parse_file_not_found(self):
        """Test that FileNotFoundError is raised for missing file."""
        print("Starting: test_parse_file_not_found")
        with self.assertRaises(FileNotFoundError):
            parse_numbers_from_file("/nonexistent/path/data.txt")

    def test_parse_invalid_number(self):
        """Test that ValueError is raised for non-integer tokens."""
        print("Starting: test_parse_invalid_number")
        filepath = self._create_test_file("1,2,abc,3")
        with self.assertRaises(ValueError):
            parse_numbers_from_file(filepath)

    def test_calculate_sum_empty(self):
        """Test sum calculation on empty list."""
        print("Starting: test_calculate_sum_empty")
        result = calculate_sum([])
        self.assertEqual(result, 0)

    def test_calculate_sum_positive(self):
        """Test sum calculation with positive integers."""
        print("Starting: test_calculate_sum_positive")
        result = calculate_sum([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)

    def test_calculate_sum_mixed(self):
        """Test sum calculation with mixed positive and negative integers."""
        print("Starting: test_calculate_sum_mixed")
        result = calculate_sum([10, -5, 20, -10])
        self.assertEqual(result, 15)

    def test_full_workflow(self):
        """Test the complete workflow: parse and sum from file."""
        print("Starting: test_full_workflow")
        filepath = self._create_test_file("10,  20, 30,40")
        numbers = parse_numbers_from_file(filepath)
        total = calculate_sum(numbers)
        self.assertEqual(numbers, [10, 20, 30, 40])
        self.assertEqual(total, 100)


if __name__ == '__main__':
    print("Running test_data_parser.py")
    unittest.main(verbosity=2)
