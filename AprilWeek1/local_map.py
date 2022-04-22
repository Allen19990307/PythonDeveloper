import pandas as pd
import requests
AK = "替换为你申请的AK"
def get_position(name, AK):
    url = f'http://api.map.baidu.com/geocoding/v3/?address={name}&output=json&ak={AK}'
    res = requests.get(url)
    val = res.json()
    retval = {'地址': name, '经度': val['result']['location']['lng'], '纬度': val['result']['location']['lat'],
              '地区标签': val['result']['level'], '是否精确查找': val['result']['precise']}
    longitude = retval['经度']
    latitude = retval['纬度']

    return (longitude, latitude)