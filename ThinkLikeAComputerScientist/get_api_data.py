import requests
def request_data(url):
    req = requests.get(url, timeout=30) # 请求连接
    req_jason = req.json() # 获取数据
    return req_jason
if __name__ == '__main__':
    url = "http://10.80.10.62:8000/dashboard_bwp/dashboard.xsodata/MATERIAL"
    print(request_data(url))

