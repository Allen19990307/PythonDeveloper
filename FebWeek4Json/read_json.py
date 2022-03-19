import json
"""python中读取文件中的内容，并更修改"""
with open("idp_backend.json",'rb') as f:
    # 获取json文件对象
    loads = json.loads(f.read())
    # 逐个遍历数组中的对象，更改数组中对应对象的值
    for item in loads['tasks']:
        item['name'] = "allen"
        item['params']['targetConfig']['table'] = "allen_keep_moving"
        item['params']['basePath'] ="/allen_keep_moving/$[yyyyMMdd-1]"
    # 写入到目标文件
    with open("json_value_change","w") as f:
        json.dump(loads,f)
        print("-------文件加载success----------")
