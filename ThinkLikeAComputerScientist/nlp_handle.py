import re

def parse(text):
    #去除标点符号和换行符
    text = re.sub(r'[^\w]]', ' ', text)

    #转换成小写的字母
    text = text.lower()

    #生成所有单词的列表
    word_list = text.split(' ')

    #去除空白的单词
    word_list = filter(None, word_list)

    #生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1

    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_cnt

with open('nlp_task','r') as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('out.txt','w') as fout:
    for word,freq in word_and_freq:
        fout.write('{} {}\n'.format(word,freq))


"""json读取"""
import json
params ={
    'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23
}
with open('params.json','w') as fout:
    params_str = json.dump(params,fout)
with open('params.json','r') as fin:
    original_params = json.load(fin)
print('type of original_params = {} ,origianl_params ={}'.format(type(original_params),original_params))

"""thinking problem 1: 使用word count实现数据读取：每次读取一部分的数据 """

"""thinking problem 2: 传输100GB文件，公司是client.py,家里的是server.py 发送数据文件"""