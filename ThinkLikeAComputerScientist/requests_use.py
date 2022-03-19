import requests

requests_get = requests.get('https://www.douban.com/')
print(requests_get.text)
