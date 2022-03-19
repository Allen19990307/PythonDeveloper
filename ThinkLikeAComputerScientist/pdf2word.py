from pdf2docx import Converter
c = Converter(r'MillionaireMindDeclarations.pdf')
c.convert(r'1.docx')
c.close()