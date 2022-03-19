#coding=utf-8
import types
import urllib as re
import json
import requests

# 利用urllib2获取网络数据
def registerUrl():
    try:
        # url = "https://www.apiopen.top/journalismApi"
        # data = re.urlopen(url).read()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        url = 'https://book.douban.com/top250'
        res = requests.get(url, headers=headers).text
        print(res)
        # data = "{\"userid\":\"ZhangJiaLin\",\"remark\":\"开心😉\"}"
        return res
    except Exception as e:
        print("get data fail")


# 写入文件
def jsonFile(fileData):
    file = open("d:\json.txt", "w")
    file.write(fileData)
    file.close()


# 解析从网络上获取的JSON数据
def praserJsonFile(jsonData):
    value = json.loads(jsonData)
    print(value)
    # rootlist = value.keys()
    # valuelist = value.values()
    # print(rootlist,valuelist)

if __name__ == "__main__":
    data = registerUrl()
    # jsonFile(data)
    # praserJsonFile(data)


