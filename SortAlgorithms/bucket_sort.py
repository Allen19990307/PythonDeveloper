from typing import List
def bucket_sort(s1:List[int]):
    min_num = min(s1)
    max_num = max(s1)
    """桶的大小"""
    bucket_size=(max_num-min_num)/len(s1)
    """桶的组数"""
    bucket_num = [[] for i in range(len(s1)+1)]
    """桶内的数据填充"""
    for i in s1:
        bucket_num[int((i - min_num)//bucket_size)].append(i)
    #     此处的下标填数没有检验出来
    s1.clear()
    for i  in bucket_num:
        for j  in sorted(i):
            s1.append(j)

# def bucket_sort(arr: List[int]):
#     """桶排序"""
#     min_num = min(arr)
#     max_num = max(arr)
#     # 桶的大小
#     bucket_range = (max_num - min_num) / len(arr)
#     # 桶数组
#     count_list = [[] for i in range(len(arr) + 1)]
#     # 向桶数组填数
#     for i in arr:
#         count_list[int((i - min_num) // bucket_range)].append(i)
#     arr.clear()
#     # 回填，这里桶内部排序直接调用了sorted
#     for i in count_list:
#         for j in sorted(i):
#             arr.append(j)




if __name__ == '__main__':
    """获取测试的数据"""
    import random
    random.seed(55)
    s1 = [random.randint(0,100) for _ in range (10)]
    bucket_sort(s1)
    print(s1)