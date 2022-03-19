import pandas as pd
# 实现读取文件所在行的位置
def finddata():
    excel = pd.read_excel(r'2.xlsx')
    s1 =[
        'Key result1',
        'Key result2',
        'main object'
    ]
    for indexs in excel.index:
        for i in range(len(excel.loc[indexs].values)):
                for j in s1:
                    if (excel.loc[indexs].values[i] == j):
                        print('行数：', indexs + 2, '列数：', i + 1)
finddata()




