"""根据归并排序进行排列"""
def merge_sort(arr):
    if len(arr) <= 1 :
        return  arr
    medium = int(len(arr)/2)
    left = merge_sort(arr[:medium])
    right = merge_sort(arr[medium:])
    return merge(left,right)
def merge(left,right):
    """对已经分治的数组实现聚合操作"""
    res = []
    i = j = k = 0
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    """A已经进入该队列,B剩余部分直接进入"""
    res = res + left[i:] + right[j:]
    return res

if __name__ == '__main__':
    nums = [5, 2, 3, 1]
    nums2 = [5, 1, 1, 2, 0, 0]
    sort = merge_sort(nums)
    print(sort)
