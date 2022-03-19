from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import ContentStream
from PyPDF2.generic import TextStringObject, NameObject
from PyPDF2.utils import b_


def remove_watermark(input_file, output_file):
    """
    pdf去除水印
    :param input_file:
    :param output_file:
    :return:
    """
    with open(input_file, "rb") as f:
        # 读取pdf文件
        source = PdfFileReader(f, "rb")
        # 创建pdf输出对象
        output = PdfFileWriter()

        for page in range(source.getNumPages()):
            # 获取pdf一页属性信息
            page = source.getPage(page)

            # 获取pdf一页的内容
            content_object = page.getContents()
            # content_object = page["/Contents"].getObject()
            # 将内容对象进行转换
            content = ContentStream(content_object, source)
            for operands, operator in content.operations:
                # 根据要去除的水印格式是“Tj”文本
                if operator == b_("Tj"):
                    # 将获取的文本替换为空
                    operands[0] = TextStringObject('')
            # 转换原来的内容对象
            page.__setitem__(NameObject('/Contents'), content)
            # 增加到新的pdf上
            output.addPage(page)

        # 输入新的pdf文件
        with open(output_file, "wb") as outputStream:
            output.write(outputStream)