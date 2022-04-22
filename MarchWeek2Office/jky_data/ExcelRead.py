import openpyxl
from openpyxl import Workbook
import pandas as pd
if __name__ == '__main__':
    path = 'D:\DeveloperLife\PythonDeveloper\MarchWeek2Office\jky_data\yogurt.xlsx'
    wb = openpyxl.load_workbook(path)
    print(type(wb))
    for x in wb.sheetnames:
        # 把元数据的内容写入Excel模板里面
        print(x)
        wb.close()
    wb.close()



