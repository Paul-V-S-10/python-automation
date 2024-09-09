from openpyxl import Workbook, load_workbook

wb = load_workbook('Book2.xlsx')
ws = wb.active
print(ws)