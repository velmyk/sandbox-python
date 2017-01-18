import unittest
import os

def analyze_text(filename):
    """Calculates the number of lines in a file.

    Args:
        filename: The file name to analyze.

    Raises:
        IOError: If 'filename' can not be read or doesn't exists.

    Returns: A tuple where the first element is a number of lines
        and the second one is a number of characters in a file.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return lines, chars

class TextAnalysisTest(unittest.TestCase):
    """Tests for the ''analyze_text()'' unction."""

    def setUp(self):
        """Fixture that creates text file for the text method to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as file_with_text:
            file_with_text.write('Lambda expression lambda expression.\n'
                                 'Lambda expression, lambda expression,\n'
                                 'Lambda expression lambda expression.')
    def tearDown(self):
        """Method that deletes files used by test method."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function runs."""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], 3)

    def test_characters_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 111)

    def test_no_such_file(self):
        """Checks the proper exception is thrown if no suh file exists."""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Checks that the function doesn't delete input file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()
