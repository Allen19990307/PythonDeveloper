"""快速排序的实现方式"""
def quick_sort(s1,left,right):
    if left >= right:
        return
    povit = partition(s1, left, right)
    quick_sort(s1,left,povit - 1)
    quick_sort(s1,povit + 1,right)
def partition(s1, left, right):
    pivot = s1[right]
    i = left
    for j in range(left,right):
        if s1[j] <pivot:
            tmp = s1[i]
            s1[i] = s1[j]
            s1[j] = tmp
            i += 1
    tmp = s1[i]
    s1[i] = s1[right]
    s1[right] = tmp
    return i
if __name__ == '__main__':
    """实现快排算法的难点在于如何设计partition这个分区"""
    s1 = [1,2,31,23,34,45,314,3,45,43,415]
    lens = len(s1)
    quick_sort(s1,0,lens - 1)
    print(s1)