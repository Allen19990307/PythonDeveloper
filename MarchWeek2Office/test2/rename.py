from openpyxl import load_workbook
wb = load_workbook('qunmaiMongoDB数据源表格的整理.xlsx')
sheet_names = wb.get_sheet_names()
for sheet_name in sheet_names:
    ws = wb[sheet_name]
    ws.title = sheet_name