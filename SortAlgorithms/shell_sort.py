"""实现希尔排序"""
def shell_sort(arr):
    def shell_insert(arr,d):
        n =len(arr)        #计算数组的长度
        for i in range(d,n):
            j = i -d
            temp = arr[i]
            while(j >= 0 and arr[j] > temp): #从后往前，寻找比其小的数的位置
                arr[j+d]=arr[j]
                j-=d
            if j != i - d:
                arr[j+d] = temp

    n = len(arr)
    if n<= 1:
        return arr
    d = n//2               #列表的跨度
    while d >= 1:
        shell_insert(arr,d)
        d = d//2
    return arr

if __name__ == '__main__':
    arr=  [5, 1, 1, 2, 0, 0]
    sort_1 = shell_sort(arr)
    print(sort_1)