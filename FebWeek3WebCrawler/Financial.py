import requests
url ='http://www.sse.com.cn/disclosure/fund/announcement/c/new/2022-01-24/510020_20220124_1_1x0Bkzsl.pdf'
requests_get = requests.get(url)
file = open('汇添富沪深300交易型开放式指数证券投资基金2021年第4季度报告.pdf', 'wb')
file.write(requests_get.content)
file.close()

