import unittest
import pathlib


class MyFileTypeTestCase(unittest.TestCase):

    def setUp(self):
        self.GTN_file_extension = pathlib.Path("data_pass/GTN.xlsx").suffix
        self.payslip_format_file_extension = pathlib.Path("data_pass/Payrun.xlsx").suffix

    def tearDown(self):
        self.GTN_file_extension = ""
        self.payslip_format_file_extension = ""

    def test_check_both_files_are_excel_files(self):
        self.assertEqual(self.GTN_file_extension, self.payslip_format_file_extension)

    def test_check_GTN_file_is_not_a_execl_file(self):
        self.GTN_file_extension = pathlib.Path("data_fail/bad_file.txt").suffix
        self.assertNotEqual(self.GTN_file_extension, self.payslip_format_file_extension)

    def test_check_payrun_file_is_not_a_execl_file(self):
        self.payslip_format_file_extension = pathlib.Path("data_fail/bad_file.txt").suffix
        self.assertNotEqual(self.GTN_file_extension, self.payslip_format_file_extension)

    def test_check_both_files_are_not_execl_files(self):
        self.GTN_file_extension = pathlib.Path("data_fail/bad_file.txt").suffix
        self.payslip_format_file_extension = pathlib.Path("data_fail/bad_file.txt").suffix
        self.assertNotEqual(self.GTN_file_extension, self.payslip_format_file_extension)


if __name__ == '__main__':
    unittest.main()
