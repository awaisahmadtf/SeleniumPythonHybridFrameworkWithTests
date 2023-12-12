from utilities import ExcelReader


# print(excelReader.get_cell_data("excelFiles/TestExcelFile.ods", "LoginTest", 2, 2))
# print(excelReader.get_data_from_excel("excelFiles/TestExcelFile.ods", "LoginTest"))
# print(excelReader.set_cell_data("excelFiles/TestExcelFile.ods", "LoginTest", "9", "9", "net"))
# print(excelReader.get_col_count("excelFiles/TestExcelFile.ods", "LoginTest"))
print(ExcelReader.get_row_count("excelFiles/TestExcelFile.ods", "LoginTest"))
