#conding=utf8
import fileinput
import os
# 获取目录下的全部文件
g = os.walk(r"/test")
for path,dir_list,file_list in g:
    for file_name in file_list:
         join = os.path.join(path, file_name)
         #逐个删除文件的第一行
         for line in fileinput.input(join, inplace=1):
             if not fileinput.isfirstline():
                 print(line.replace('\n',''))
