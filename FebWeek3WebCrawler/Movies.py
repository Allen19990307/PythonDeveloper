import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
url = 'https://book.douban.com/top250'
res = requests.get(url,headers = headers).text
p_rate = '<span class="rating_num" property="v:average">(.*?)</span>.*?</div>'
rate =  re.findall(p_rate, res, re.S)

def db(page):
    num = (page - 1) * 25 #根据当前页面参数的规律
    print('num:   '+str(num))
    url = 'https://movie.douban.com/top250?start='+str(num)
    res = requests.get(url,headers = headers).text
    """根据web的源代码，使用正则表达式去提取数据 1.注意这边的格式问题，需要和原本页面代码保持一致"""
    # p_title = '<img width="100" alt="(.*?)"'
    # title = re.findall(p_title,res) # 提取影片的名称
    # p_img = '<img width="100" alt=".*?" src="(.*?)"'
    # img = re.findall(p_img,res) # 获取图片所在的网址
    # Method2
    # p_num ='<em class>(.*?)</em>'  原本的提取功能改用手写
    # num = re.findall(p_num,res)
    p_img = '<div class="pic">.*?src="(.*?)"'
    img = re.findall(p_img, res, re.S)
    p_title = '<span class="title">(.*?)</span>.*?</div>'
    title = re.findall(p_title, res, re.S)
    p_rate = '<span class="rating_num" property="v:average">(.*?)</span>.*?</div>'
    rate = re.findall(p_rate, res, re.S)

    """提取电影的图片"""
    for i in range(len(title)):
        print(str(num+ i + 1)+'.'+title[i])
        print(img[i])
        res = requests.get(img[i])
        file = open('Movies/' +str(num+i+1)+ ' '+title[i] +' '+rate[i]+ '.jpg', 'wb')#创建images文件夹，以片名作为图片文件名
        file.write(res.content)
        file.close()

for i in range(10):
    db(i + 1)
    print('第' + str(i + 1) + '页爬取Success')
