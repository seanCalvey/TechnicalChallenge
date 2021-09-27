import unittest
import pandas as pd


def check_columns_type(series):
    for cell_type in series.values:
        if cell_type == "int" or "float":
            print(cell_type)
        elif cell_type == object:
            return False
    return True


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.GNT_file = pd.read_excel("data_fail/GTN_String.xlsx")

    def test_data_cell_in_GNT_are_numeric(self):
        pay_elements = self.GNT_file.dtypes[4:]
        self.assertTrue(check_columns_type(pay_elements))


if __name__ == '__main__':
    unittest.main()
