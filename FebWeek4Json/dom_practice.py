from xml.dom.minidom import parse
# 获取
# 读取文件
dom = parse('test.xml')
# 获取文档元素对象
data = dom.documentElement
#获取 student
stus = data.getElementsByTagName('student')
for stu in stus:
    # 获取标签的属性值
    stu_get_id = stu.getAttribute('id')
    stu_get_name = stu.getAttribute('name')
    # 获取标签中的内容
    id = stu.getElementsByTagName('id')[0].childNodes[0].nodeValue
    name = stu.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = stu.getElementsByTagName('age')[0].childNodes[0].nodeValue
    gender = stu.getElementsByTagName('gender')[0].childNodes[0].nodeValue
    print('st_id',stu_get_id,'st_name',stu_get_name)
    print('sid',id,'name',name,'age',age,'gender',gender)
