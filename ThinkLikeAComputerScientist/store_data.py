from pathlib import Path
from urllib import request
import pandas as pd
import urllib
# python的使用熟练度
def fix_missing(x):
    return False if x in ["","MISSING"] else x
def fetch_data(url):
    # 爬虫组的实现
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0')
    with request.urlopen(req) as f:
        return f
if __name__ == '__main__':
    df = pd.read_excel("xl/stores.xlsx", sheet_name="2019", skiprows=1,
                       usecols="B:F",converters={"Flagship":fix_missing})
    print(df)
    sheets = pd.read_excel("xl/stores.xlsx", sheet_name=["2019","2020"], skiprows=1,
                           usecols=["Store","Employees"])
    print(sheets["2019"].head(2))
    df1 = pd.read_excel("xl/stores.xlsx", sheet_name=0, skiprows=2,skipfooter=3,
                           usecols="B:C,F",header = None,
                           names=["Branch","Employee_Count","Is_Flagship"])
    print(df1)
    df = pd.read_excel("xl/stores.xlsx", sheet_name="2019", skiprows=1,
                       usecols="B,C,F",skipfooter=2,
                       na_values="MISSING",keep_default_na=False)
    print(df)
    # with保证文件会被正常关闭
    # with open("output.txt","w") as f:
    #     f.write("allen keeps iterating")

    with pd.ExcelFile("xl/stores.xlsx") as f:
        df1 = pd.read_excel(f, "2019", skiprows=1, usecols="B:F", nrows=2)
        df2 = pd.read_excel(f, "2020", skiprows=1, usecols="B:F", nrows=2)

    print("---------------------------------")
    url = ("https://gitee.com/ChanAllen/python-for-excel/blob/1st-edition/xl/stores.xlsx")
    # df1 = pd.read_excel(url, skiprows=1, usecols="B:E", nrows=2)
    # print(df1)

    print(fetch_data(url))