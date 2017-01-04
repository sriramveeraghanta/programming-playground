from xlrd import open_workbook
book_name = raw_input("Enter excel file path")
book = open_workbook(book_name)
sheet = book.sheet_by_index(0)
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        data = str(sheet.cell(i, j).value)
        print(data)
