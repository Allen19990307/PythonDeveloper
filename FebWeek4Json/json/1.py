import json
"""python中读取文件中的内容，并更修改"""
with open("1.json",'rb') as f:
    loads = json.loads(f.read())
    # print(loads)
    for item in loads['heart']:
        # loads.timeout = 444
        item['will'] = "爱"
        print(item['will'][0])

        # item['everything']['basePath'] ="/sftpuser/qunmai_mongodb/product/$[yyyyMMdd-1]"
    print(loads)
    # with open("json_value_change","w",encoding='utf-8') as f:
    #     json.dump(loads,f)
    #     print("-------文件加载success----------")





















