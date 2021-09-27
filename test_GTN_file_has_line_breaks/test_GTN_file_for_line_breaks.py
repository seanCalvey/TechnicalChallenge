import unittest
import pandas as pd
# had to import openpyxl


class MyLineBreakTestCase(unittest.TestCase):

    def setUp(self):
        self.GTN_df = pd.read_excel("data_pass/GTN.xlsx")

    def tearDown(self):
        self.GTN_df = ""

    def test_GTN_file_with_no_line_breaks(self):
        dropped_line_breaks = self.GTN_df.dropna(how="all")
        self.assertEqual(len(dropped_line_breaks), len(self.GTN_df))

    def test_GTN_file_with_line_breaks(self):
        self.GTN_df_with_line_breaks = pd.read_excel("data_fail/GTNWithLineBreaks.xlsx")
        dropped_line_breaks = self.GTN_df_with_line_breaks.dropna(how="all")
        self.assertNotEqual(len(dropped_line_breaks), len(self.GTN_df_with_line_breaks))


if __name__ == '__main__':
    unittest.main()
