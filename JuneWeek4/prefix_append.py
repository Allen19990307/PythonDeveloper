import os
import sys
"""给当前的项目文件的末尾添加后缀"""
if __name__ == "__main__":
    folder_name = "/Users/allen/PycharmProjects/PythonDeveloper/JuneWeek4/order"  # 获取文件夹的名字，即路径
    file_names = os.listdir(folder_name)  # 获取文件夹内所有文件的名字

    for name in file_names:  # 如果某个文件名在file_names内
        old_name = folder_name + '/' + name  # 获取旧文件的名字，注意名字要带路径名
        new_name = folder_name + '/' + 'cdw_' + name   # 定义新文件的名字，这里给每个文件名前加了前缀 a_
        os.rename(old_name, new_name)  # 用rename()函数重命名
        print(new_name)  # 打印新的文件名字
