"""线性排序第二弹：基数排序"""
# what: 基数排序，从小到大，根据每位数字的大小排列
# why:  线性排序的效率更高
# how:  一般规律，实现功能
def radix_sort(s1):
    n = len(str(max(s1)))
    # 清楚是几轮排序
    for k in range(n):
        bucket_list=[[]for i in range(10)]
        for i in s1:
            bucket_list[i//(10 ** k) % 10].append(i)
        s1 = [j for i in bucket_list for j in i ]
    return s1

    # 法一暴力拆解：回到实际
    # for i in range(len(s1)-1):
    #     for j in range(i):
    #         if(s1[j] % 10 < s1[j+1] % 10):
    #             temp = s1[i]
    #             s1[i] = s1[i+1]
    #             s1[i+1] = temp
    # for i in range(len(s1)-1):
    #     for j in range(i):
    #         if(s1[j] // 10 < s1[j+1] // 10):
    #             temp = s1[i]
    #             s1[i] = s1[i+1]
    #             s1[i+1] = temp


if __name__ == '__main__':
    import random
    # seed便于生成相同的数字
    random.seed(55)
    s1 = [random.randint(0,100) for _ in range(10)]
    print("排序之前")
    print(s1)
    print(radix_sort(s1))
    print(s1)

    """为什么原数组的内容没有修改呢？"""