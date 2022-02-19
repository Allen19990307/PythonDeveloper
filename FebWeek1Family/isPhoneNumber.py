# 为何我们需要正则表达式？简化代码，完善功能
import re
# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
#     return True

"正则的魅力：创造可复制的成功模式，可迭代式成长"
# message = 'The core ability that Allen has (416)-202-4243，(415)-202-4242'
# re_compile = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
# search = re_compile.findall(message)
# print('Phone number found: '+'地区：')
# print(search)

# re_compile.search('')
# for i in range(0,len(message)-11):
#     if isPhoneNumber(message[i:i+12]):
#         number = message[i:i+12]
#         print(f"The message contains {number}")
# print(f"Mission is over.")
# print('判断415-202-4242是否符合标准的电话号码')
# print(isPhoneNumber('415-202-4242'))

"""正则表达式，模式匹配的选择"""
# pattern = re.compile(r'Allen&Gu(Data|Stanford|Sports|Business)')
# pattern_search = pattern.search('Allen&GuStanford')
# group = pattern_search.group()
# print(group+' '+pattern_search.group(1))

"""这边的模式匹配，？表示可选匹配"""
# pa = re.compile(r'Super(wo)?man')
# pa_search = pa.search('The adventure of Superman')
# print(pa_search.group())
# match_one = pa.search('The adventure of Superwoman')
# print(match_one.group())

# 是否包含区号 ？0次或者1次前面的分组
# p = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# p_search = p.search('My number is 123-321-1999')
# s1 = p_search.group()
# print(s1)
# p_search2 = p.search('My number is 321-1999')
# s2 = p_search2.group()
# print(s2)

# * 的使用，紧靠符号的使用  0次或者多次前面的分组
# pa = re.compile(r'Super(wo)*man')
# pa_search = pa.search('The adventure of Superwowowoman')
# print(pa_search.group())

# + 的使用   1次或者多次前面的分组
# pa = re.compile(r'Super(wo)+man')
# pa_search = pa.search('The adventure of Superwowowoman')
# print(pa_search.group())

#{} 花括号的使用,可选择重复出现的次数区间范围
#{n,m}匹配至少n次，至多m次前面的分组，后加？表示进行非贪心匹配
# compile1 = re.compile(r'(Ha){3,5}?')
# compile__search = compile1.search('HaHaHaHa')
# search_group = compile__search.group()
# print(search_group)

# 字符分类  缩短我们使用的编程长度
# p1 = re.compile(r'\d+\s\w+')
# findall = p1.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, ' \
#                      '6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(findall)

# 建立自己的字符分类   ^代表必须比aeiouAEIOU开头
# compile2 = re.compile(r'[^aeiouAEIOU]')
# match_none = compile2.search('Experience')
# print(match_none.group())

# 插入字符和美元字符
# p2 = re.compile(r'Hello$')
# p__search = p2.search('Hello basketball')
# p__search1 = p2.search('basketball Hello')
# print(p__search1)
# +$ 获取从头到尾都是数字结尾的数
# \d \w \s 分别匹配数字、单词和空格 \D \W 和\S 分别匹配数字，单词，空格之外的所有字符
# [abc]匹配方括号内的任意字符如a、b或c  [^abc]表示不在方括号内的任意字符
# re_compile1 = re.compile(r'\d+$')
# m = re_compile1.search('Your number is 3134')
# print(m)

# . 匹配所有的换行符号，除了换行符
# compile3 = re.compile(r'.ind')
# l = compile3.findall('We have a mind to go over the road.')
# print(l)

# . * 的集合使用
# p3 = re.compile(r'First Name: (.*) Last Name: (.*)')
# m1 = p3.search('First Name: Al Last Name: Smith')
# print(m1.group(1))
# print(m1.group(2))

# .*?组合使用，匹配所有的文本  和大括号使用，非贪心模式
# compile4 = re.compile(r'<.*?>')
# m2 = compile4.search('<To serve man> for dinner')
# print(m2.group())

# 句点字符匹配换行符外的所有字符
# compile5 = re.compile('.*')
# law___group = compile5.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# print(law___group)
# compile6 = re.compile('.*', re.DOTALL)
# s = compile6.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# print(s)

# 忽视大小写,模式匹配
# robocop = re.compile('RoboCop', re.IGNORECASE)
# cop___group = robocop.search('RoboCop is part man, part machine, all cop.').group()
# print(cop___group)
# innocent___group = robocop.search('ROBOCOP protects the innocent.').group()
# print(innocent___group)
# much__group = robocop.search('Al, why does your programming book talk about robocop so much?').group()
# print(much__group)

# 不分大小写的匹配
# robocop = re.compile(r'Robocop', re.I)
# cop__group = robocop.search('robocop is part man,part machine,all cop').group()
# print(cop__group)
# the_innocent___group = robocop.search('robocop protects the innocent.').group()
# print(the_innocent___group)
# so_much__group = robocop.search('Al,why does your programming book talk about robocop so much?').group()
# print(so_much__group)

# sub()方法进行替换
# compileRegex = re.compile(r'Agent \w+')
# regex_sub = compileRegex.sub('CONSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# print(regex_sub)

# pattern = re.compile(r'Agent (\w)\w*')
# sub = pattern.sub(r'\1****', 'Agent Allen told Agent Chris that Agent Dorothy was a double agent.')
# print(sub)

re.compile(r'''(
  (\d{3}|\(\d{3}\))?   #area code
  (\s|-|\.)?           #separator
)''')