import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
print(type(sheet))
cells = tuple(sheet.columns)   # アクティブなセルのうち、columnがBの列を取得
print(cells[1])
for cell in cells[1]:
    print(cell.coordinate, cell.value)
