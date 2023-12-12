import pyexcel_ods


def get_row_count(path, sheet_name):
    workbook = pyexcel_ods.get_data(path)
    sheet = workbook[sheet_name]
    return len(sheet)


def get_col_count(path, sheet_name):
    workbook = pyexcel_ods.get_data(path)
    sheet = workbook[sheet_name]
    max_col = 0
    for r in range(len(sheet)):
        if len(sheet[r]) > max_col:
            max_col = len(sheet[r])

    return max_col


def get_cell_data(path, sheet_name, row_number, column_number):
    workbook = pyexcel_ods.get_data(path)
    sheet = workbook[sheet_name]
    # return sheet[row_number][column_number]
    for index, row in enumerate(sheet):
        if index + 1 == int(row_number):
            for index1, cell in enumerate(row):
                if index1 + 1 == int(column_number):
                    if cell != "":
                        return cell
                    else:
                        return "Cell is empty"


def set_cell_data(path, sheet_name, row_number, column_number, data):
    workbook = pyexcel_ods.get_data(path)
    sheet = workbook[sheet_name]
    # Extend the rows if necessary
    while len(sheet) <= row_number:
        sheet.append([''] * (column_number -1))

    # Extend the columns if necessary
    for row in sheet:
        while len(row) <= column_number-1:
            row.append('')

    # Now, you can safely add the data to the specified cell
    sheet[row_number-1][column_number-1] = data

    # Save the updated data back to the ODS file
    pyexcel_ods.save_data(path, {sheet_name: sheet})
    return "Cell Value Updated"


def get_data_from_excel(path, sheet_name):
    data_list = []
    workbook = pyexcel_ods.get_data(path)
    sheet = workbook[sheet_name]
    total_rows = len(sheet)
    total_columns = len(sheet[0])

    for r in range(1, total_rows):
        row_list = []
        for c in range(total_columns):
            row_list.append(sheet[r][c])
        data_list.append(row_list)

    return data_list
