from pdf2docx import Converter
pdf_file = '【大数据底座第三方技术服务支持采购】邀请招标 - 技术回标文件格式.pdf'
docx_file ='1.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()