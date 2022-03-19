from docx2pdf import convert
import os
from docx2pdf import convert
import os
"""目标文件夹里存放你所需要的word文件"""
director = r'D:\workspace\word2pdf'
FileList = map(lambda x: director + '\\' + x, os.listdir('D:\workspace\word2pdf'))
for file in FileList:
    convert(file, f"{file.split('.')[0]}.pdf")

