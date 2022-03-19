import xml.etree.ElementTree as ET
# 使用ElementTree的使用方式
tree = ET.parse("test.xml")
# 获取根节点
root = tree.getroot()
# 标签名
print('root_tag:',root.tag)
for stu in root:
    # 属性值
    print("stu_name:",stu.attrib["name"])
    # 标签内容
    print("id: ",stu[0].text)
    print("name: ",stu[1].text)
    print("age: ",stu[2].text)
    print("gender: ",stu[3].text)


