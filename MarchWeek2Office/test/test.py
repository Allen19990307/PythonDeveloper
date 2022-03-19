import openpyxl
import xlwings as xw
import pandas as pd

df = pd.read_excel('mongodb数据字典(1).xlsx', usecols=[0],header=1)
df.to_excel(r'123.xlsx',startrow=1,index = False)

wb = openpyxl.load_workbook('123.xlsx')
sheet = wb.active
sheet.title = '表结构'
sheet['A1'] ='字段名'
sheet['B1'] = '类型'
sheet['B2'] = 'string'
sheet['C1'] ='精度1'
sheet['D1'] ='精度2'
sheet['E1'] ='字段描述'
wb.save('123.xlsx')

# list1 = [[1],[2],[3],[4],[5]]
# sht = xw.Book().sheets('sheet1')  # 新增一个表格
# sht.range('A1').value = list1