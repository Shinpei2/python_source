import openpyxl

wb = openpyxl.Workbook()

print(wb.get_sheet_names())

sheet = wb.active


sheet.title = 'Spam Bacon Eggs Sheet'
print(sheet.title)