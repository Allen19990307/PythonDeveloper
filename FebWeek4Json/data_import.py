import requests
import sys
# sys.setdefaultencoding("utf-8")
def pdf(url):
    pdf= requests.get(url)
    result = pdf.text
    print(result)
    # try:
    #     with open('/data/idp/python12345.txt', 'wb') as f:
    #         f.write(result)
    # except:
    #     print("data break")
if __name__ == '__main__':
    pdf('http://10.80.10.62:8000/dashboard_bwp/dashboard.xsodata/MATERIAL?$format=json')
