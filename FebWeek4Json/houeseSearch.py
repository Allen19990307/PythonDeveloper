from urllib import request
from bs4 import BeautifulSoup
import chardet
"""使用urllib进行网页页面的爬取"""
url = "https://sh.lianjia.com/zufang"
# 发送请求等待接受响应
response = request.urlopen(url)
# 调用read方法读取并且转换为utf-8的编码格式
html = response.read()
#获取文本编码
html_encoding = chardet.detect(html)
#文本转换编码
content = html.decode(html_encoding['encoding'])
print(content)