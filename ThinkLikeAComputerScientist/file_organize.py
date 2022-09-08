import shutil,os,send2trash
from pathlib import Path

"""查看当前的路径"""
p = Path.home()
# shutil.copy(p/'Desktop/sku_交易.sql',p/'Desktop/test')
print(p)

"""遍历当前文件中含txt文件"""
for filename in Path.home().glob('*.txt'):
    print(filename)

"""移除business文件"""
# baconFile = open('business', 'a')
# baconFile.write('Being an entrepreneur.')
# baconFile.close()
# send2trash.send2trash('business')

"""遍历当前的文件夹"""
for foldername,subfolders,filenames in os.walk('/Users/allen/Desktop'):
    print('The current folder is '+foldername)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + foldername + ': '+subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + foldername + filename)
    print('')








