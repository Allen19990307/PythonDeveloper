import fitz
import os

doc = fitz.open()

# jpg文件路径： 当前文件夹下的files文件夹
img_path = os.path.join(os.path.abspath(os.curdir), 'files')

# 避免顺序错误，将1.jpg, 2.jpg ... 10.jpg等前面补零变为01.jpg, 02.jpg等
for img_file in os.listdir(img_path):
    new_name = ('0000' + img_file)[len(img_file)-3:] #长度对齐
    os.rename(os.path.join(img_path, img_file), os.path.join(img_path, new_name))

# 转换为pdf格式后合并
for img_file in os.listdir(img_path):
    full_name= os.path.join(img_path, img_file)
    pdfbytes = fitz.open(full_name).convert_to_pdf()
    imgpdf = fitz.open(img_file + '.pdf', pdfbytes)
    doc.insert_pdf(imgpdf)

doc.save('Allen.pdf')
doc.close()
