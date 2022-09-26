if __name__ == '__main__':
    #极客时间 python开发工程师  class one
    """1. 列表不支持更改，元组支持; 2.元组的性能要优于列表，其存储的字段个数更早 """
    #对数组和元组进行切片操作
    a1 = (1,2,3,4)
    a2 = [1,2,3,4]
    a2.append(5)
    print(a2[1:3])

    #基本的的操作：sort，count等
    print(a1.count(4))

    #效率的比较：
    arrya_list = list()
    arrya_list1 = []

    #class two
    """1.字典和集合 注意：集合不支持索引，其本质为哈希表，"""
    d1 = {'name':'jason','age':'20','gender':'male'}
    d2 = dict({'name':'jason','age':'20','gender':'male'})
    d1.pop('name')
    d1['bob'] = '2022-12-01'
    print(d1 == d2)
    print(d1)

    """寻找仓库里是否拥有对应的产品id号"""
    def find_product_price(products,product_id):
        for id , price in products:
            if id == product_id:
                return price
        return None
    products = [ (143121312, 100),
                 (432314553, 312),
                 (32421912367, 150) ]
    #参数的名称
    print('The price of product 432314553 is {}'.format(find_product_price(products,432314553)))

    """查看仓库里对应有多少的价格，并且返回列表里所有价格的个数"""
    def find_unique_price_using_list(products):
        unique_price_list = []
        for _,price in products:
            if price not in unique_price_list:
                  unique_price_list.append(price)
        return len(unique_price_list)
    products = [(143121312, 100), (432314553, 30), (32421912367, 150), (937153201, 30)]
    print('number of unique price is : {}'.format(find_unique_price_using_list(products)))
    #class three
    """string use,单独的制表符号使用"""
    name = 'jason'
    city = 'beijing'
    text = 'welcome to China'
    s = 'a\nb\tc'
    print(s)
    name = 'jason'
    """string的字符串是不能改变的"""
    print(name[0]+''+name[1:3])
    s1 = 'hello'
    """2.5版本之前的python使用的额是重新分配一块内存来创建新的字符串并且拷贝"""
    """2.5版本之后的python在原油的基础的上扩充字符串buffer的大小"""
    s2 = 'H' + s1[1:]
    s3 = s1.replace('h', 'H')
    print(s2)

    """使用split函数"""
    def query_data(namespace,table):
       """
       api函数的调取和应用
       :param namespace:
       :param table:
       :return:
       """


    path = 'hive://ads/training_table'
    namespace = path.split('//')[1].split('/')[0]
    print(namespace)
    table = path.split('//')[1].split('/')[1]
    #query_data(s1,s2)

    """计算开头和结尾的空字符串"""
    s = 'my name is jason'
    print("去除开头"+s.lstrip()+" 去除结尾"+s.rstrip()+" 去除首尾"+s.strip())

    id = '0096'
    name = 'Allen'
    #method one  当前的最新规范
    print('no data available for person with id:{},name:{}'.format(id,name))
    #method two
    print('no data available for person with id: %s,name: %s' % (id,name))

    #在原有的基础上直接进行连接，方案一，数据较少的时候，拼接效果更高
    s = ''
    for n in range(0, 100000 ):
        s += str(n)
    #print(s)


    """使用' '连接序列"""
    l = []
    for n in range(0,100000):
        l.append(str(n))
    s = ' '.join(l)
    #print(s)

    """class five:input and output"""
    # name = input('your name:')
    # gender = input('you are a boy?(y/n)')


    #prefix = 'you are the master of your world.'
    #welcome_str = 'Welcome to the matrix, you are the master of your world, {prefix} {name}'
    welcome_dic = {
        # 'prefix':'Mr.' if gender == 'y' else 'Mrs',
        # 'name' : name
    }
    print('loading....')
    #print(welcome_str.format(**welcome_dic))

    """关注是否有数据的相加"""
    a = input()
    b = input()
    print('a + b = {}'.format(a + b))
    print('a + b = {}'.format(int(a) + int(b)))


