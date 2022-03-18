import openpyxl


def create_workbook(name):
    wb = openpyxl.Workbook
    wb.active.title = 'Sheet1'        # renames the active sheet
    # wb.create_sheet('Sheet2')       # create a 2nd sheet
    wb.save(name)

    return wb


def read_sheet(sheet):
    rows = sheet.iter_rows()       # return generator class
    # print(type(rows))

    for row in rows:
        # print(row)
        for cell in row:
            print(cell.value)


def find_and_replace(wb, old, new):

    rows = wb['Sheet1'].iter_rows()       # return generator class

    for row in rows:
        # print(row)
        for cell in row:
            if cell.value == old:
                cell.value = new

    return wb


if __name__ == '__main__':
    # wb = create_workbook('test_spreadsheet.xlsx')

    wb = openpyxl.load_workbook('test_spreadsheet.xlsx')
    print(wb.sheetnames)

    wb = find_and_replace(wb, 'John', 'Jim')
    wb.save('test_spreadsheet.xlsx')
    read_sheet(wb['Sheet1'])
