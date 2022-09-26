"""select_sort 选择排序
you chose a minimum word in unsorted array and exchange it"""
def select_sort(arr):
    n = len(arr)
    if  n <= 1:
        return arr
    for i  in range (0 , n-1):
        minIndex = i
        for j in range( i+1 ,n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            (arr[minIndex],arr[i])=(arr[i],arr[minIndex])
    return arr

def select_sort1(arr):
    n = len(arr)
    for i in range(0,n-1):
        minIndex = i
        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        """对剩余队列的整体完成循环，最后再去交换数字"""
        if minIndex != i:
                (arr[minIndex],arr[i]) = (arr[i],arr[minIndex])
    return arr


if __name__ == '__main__':
    arr = [1,2,3412,121,13,23,10]
    print(select_sort1(arr))