#学会使用快捷键1
#Demo1  格式转换
print(int(3.17))
print(float(6))

#Demo2  列表   学会使用列表的嵌套功能
list_data = ['Allen','entrepreneur',23]
list_data1 = [['Michael','teacher'],(1,2,3),{'Name':'Allen','Hobbies':'Read & Run'}]
print(list_data)
print(list_data1)

#Demo3 修改个人信息
#增
person_info =['Allen','Male']
person_info.append(1.80)  #增加自己的身高
person_info.insert(1,23) #增加自己的年龄
print(person_info)
#改
person_info[3]=1.81 #为自己增高，哈哈
person_info[0:2]=['Handsome boy',18+1] #为自己带盐（哦，代言）
print(person_info)
#查
print(person_info[2])
print(person_info[0:2])
#删
person_info.pop(2) #基于索引
print(person_info)  #堆栈  push pop
person_info.remove(19)#基于内容
print(person_info)
del person_info[0:2] #基于索引删除
print(person_info)
person_info.clear()#删除全部列表的元素
del person_info #删除整个列表
#总结：1.查询：无需由数可替换数据   修改需要  2.pop 默认删除最后一个，如果有指定，那就删除指定的内容


#Demo3  字典
dict_1 = dict() #空值创建
dict_2 = {}
#非空值创建的三种方式
dict_3 = {'姓名':'Allen','年龄':23}
dict_4 = dict({'Name':'小龙人','Age':'23'})
dict_5 = dict(name='金丝猴',age=23)

#python中的字典表里有的是item，item由键值对组成   []() 外不加‘’ ，防止编程字符串
dict_6 = {'Name':('Michael','Allen'),'cities':['Beijing','Shanghai']}
print(dict_6)

info = {'Name':'Allen','City':'Shanghai','Job':'Data analyst'}
print(info)
#增删改查  操作
info['Desire']='Entrepreneur'
info['City']='San Francisco';
print(info['Name'])
del info['Job']
print(info)






