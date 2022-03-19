import time
import pymssql
import requests
from bs4 import BeautifulSoup
#  https://wh.lianjia.com/zufang/
#获取url中下面的内容
def get_page(url):
  responce = requests.get(url)
  soup = BeautifulSoup(responce.text,'lxml')
  return soup
#封装成函数，作用是获取列表下的所有租房页面的链接，返回一个链接列表
def get_links(url):
  responce = requests.get(url)
  soup = BeautifulSoup(responce.text,'lxml')
  link_div = soup.find_all('div',class_ = 'pic-panel')
  links = [div.a.get('href') for div in link_div]
  return links
#收集一个房子的信息
def get_house_info(house_url):
  soup = get_page(house_url)
  price = soup.find('span',class_='total').text
  unit = soup.find('span',class_= 'unit').text[1:-1]
  area = soup.find('p', class_ = 'lf').text
  house_info= soup.find_all('p',class_ = 'lf')
  area = house_info[0].text[3:] #字符串切片工具
  layout = house_info[1].text[5:]
  info={
    '价格':price,
    '单位':unit,
    '面积':area,
    '户型':layout
    }
  return info
#链接数据库
server="127.0.0.1"  #换成自己的服务器信息
user="root"
password="123456"    #自己的数据库用户名和密码
conn=pymssql.connect(server,user,password,database="house")
def insert(conn,house):
  #sql_values = values.format(house['价格'],house['单位'],house['面积'],
                #house['户型'])
  sql = "insert into [house].dbo.lianjia(price,unit,area,layout)values('%s','%s','%s','%s')"%(house["价格"],house["单位"],house["面积"],house["户型"])
  print(sql)
  cursor = conn.cursor() #游标，开拓新的窗口
  #cursor1 = conn.cursor()
  cursor.execute(sql) #执行sql语句
  conn.commit() #提交 ，更新sql 语句
links = get_links('https://sh.lianjia.com/zufang/pudong/brp1000erp4000/')
count = 1
for link in links:
  #time.sleep(2)
  print('获取一个数据成功')
  house = get_house_info(link)
  insert(conn,house)
  print("第%s个数据，存入数据库成功！"%(count))
  count = count+1
  #print(house["价格"],end='\r')