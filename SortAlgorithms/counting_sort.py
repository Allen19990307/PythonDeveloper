def counting_sort(s1):
    """获取数组中的最大和最小值"""
    max= min = 0
    for i in s1:
        if i > max:
            max = i
        if i < min:
            min = i
    length = max - min + 1
    new_arr = [0] * length
    """定义新的数组，并给数组中每个出现的数字的次数标号"""
    for j in range(length):
        new_arr[j] = 0
    for index in s1:
        new_arr[index - min] += 1
    index = 0
    """重新给原数组排序，并赋予初始值"""
    for i in range(length):
        for j in range(new_arr[i]):
         """此处需要支持"""
         s1[index] = i + min
         index += 1


if __name__ == '__main__':
    import random
    random.seed(54)
    s1 = [random.randint(0,100) for _ in range(10)]
    print("原始的数据样本",s1)
    counting_sort(s1)
    print("当下的数据样本",s1)