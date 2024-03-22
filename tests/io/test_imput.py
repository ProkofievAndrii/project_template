import unittest
import pandas as pd
from app.io.input import read_text_from_file_builtin, read_text_from_file_with_pandas


class TestIOFunctions(unittest.TestCase):

    def test_read_text_from_file_builtin_exists(self):
        self.assertTrue(callable(read_text_from_file_builtin))

    def test_read_text_from_file_with_pandas_exists(self):
        self.assertTrue(callable(read_text_from_file_with_pandas))

    def test_from_file_builtin(self):
        expected_text = "TESTTESTTESTTEST"
        file_path = "test_builtin.txt"
        with open(file_path, 'w') as file:
            file.write(expected_text)
        text = read_text_from_file_builtin(file_path)
        self.assertEqual(text, expected_text)

    def test_from_file_with_pandas(self):
        expected_text = "TESTTESTTESTTEST"
        file_path = "test_pandas.csv"
        pd.DataFrame({"TESTTESTTESTTEST": [expected_text]}).to_csv(file_path, index=False)
        text = read_text_from_file_with_pandas(file_path)
        self.assertEqual(text, expected_text)


if __name__ == '__main__':
    unittest.main()
