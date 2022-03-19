import pandas as pd
from openpyxl import load_workbook
result2=[('a','2','ss'),('b','2','33'),('c','4','bbb')]#列表数据
writer = pd.ExcelWriter('123.xlsx',engine='openpyxl')#可以向不同的sheet写入数据
book=load_workbook('123.xlsx')
writer.book = book
df = pd.DataFrame(result2,columns=['xuhao','id','name'])#列表数据转为数据框
df.to_excel(writer, sheet_name='sheet2')#将数据写入excel中的sheet2表,sheet_name改变后即是新增一个sheet
writer.save()#保存