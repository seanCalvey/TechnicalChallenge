import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.GNT_employee_Series = pd.read_excel("data_pass/GTN.xlsx", usecols=["employee_id"], squeeze=True)
        cls.payrun_employee_Series = pd.read_excel("data_pass/Payrun.xlsx", skiprows=[1], usecols=["Employee ID"], squeeze=True)

    def test_employees_in_GTN_can_be_mapped_to_payrun(self):
        payrun_employee_Series_cleaned = self.payrun_employee_Series.dropna()
        payrun_employee_Series_reformated = payrun_employee_Series_cleaned.astype("int64")
        series_match = payrun_employee_Series_reformated.equals(self.GNT_employee_Series)
        self.assertTrue(series_match)


if __name__ == '__main__':
    unittest.main()
