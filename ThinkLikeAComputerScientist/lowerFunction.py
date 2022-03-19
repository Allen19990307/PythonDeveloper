import re
if __name__ == '__main__':
    """列表的形式存储数据"""
    s = [
        'allenBillionaireAct',
        'allenKeepMoving',

    ]
    """引入正则表达式，修改下数据的格式：将其中大写字母，转为小写，前面添加_"""
    for i in range(0,len(s)):
        sub = re.sub("[A-Z]", lambda x: "_" + x.group(0).lower(), s[i])
        print(sub)






