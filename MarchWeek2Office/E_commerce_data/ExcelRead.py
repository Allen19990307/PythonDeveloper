import csv

import openpyxl
import xlrd
from openpyxl import Workbook
import pandas as pd
if __name__ == '__main__':
    path = 'D:\DeveloperLife\PythonDeveloper\MarchWeek2Office\E_commerce_data\milk_vip.xls'
    wb = xlrd.open_workbook(path)
    with open('D:\\workspace\\Billionarie mind\\1.csv'.format(t3='13ruku1'), 'w',
              newline='') as f:
        writer = csv.writer(f)
        writer.writerows(wb)
        f.close()




