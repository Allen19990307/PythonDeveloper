# 通过城市缩写确定url
from random import random

import requests
from bs4 import BeautifulSoup

city_number = 'sh'
url = 'https://{0}.lianjia.com/zufang/'.format(city_number)

# 主起始页
self.base_url = url
# 当前筛选条件下的页面
self.current_url = url
# 设置爬虫头部
self.headers = {
    'User-Agent': self.get_ua(),
}

def get_ua(self):
    """
    在UA库中随机选择一个UA
    :return: 返回一个库中的随机UA
    """
    ua_list = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
    ]

    return random.choice(ua_list)


def get_house_count(self):
    """
    获取当前筛选条件下的房屋数据个数
    @param text:
    @return:
    """
    # 爬取区域起始页面的数据
    response = requests.get(url=self.current_url, headers=self.headers)
    # 通过 BeautifulSoup 进行页面解析
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获取数据总条数
    count = soup.find_all(class_='content__title--hl')[0].string

    return soup, count
    # 获取当前筛选条件下数据总条数
    soup, count_main = self.get_house_count()

    # 如果当前当前筛选条件下的数据个数大于最大可查询个数，则设置第一次查询条件
    if int(count_main) > self.page_size*self.max_pages:
        # 获取当前城市的所有区域，当做第一个查询条件
        pass
    else:
        # 直接遍历获取数据
        pass