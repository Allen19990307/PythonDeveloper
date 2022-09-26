"""对排序的实现
子节点 大于/小于  父节点的大小
"""
def heap_sort(arr):
    def heap_adjust(arr,start,end):#start根结点为大顶堆
       temp = arr[start]
       son = 2 * start + 1 #子节点的计算
       while son <= end:
           if son < end and arr[son] < arr[son + 1]: #找出左右孩子节点较大的数
               son += 1
           if temp >= arr[son]: #判断是否为大顶堆
               break
           arr[start] = arr[son] #子节点上移
           start = son
           son = 2 * son + 1
       arr[start] = temp   #将原堆顶插入正确位置
    """直接返回特殊的情况"""
    n = len(arr)
    if n <= 1:
        return arr

    """root根结点，逐渐归为0"""
    #建立大顶堆
    root = n // 2 - 1 #完全二叉树
    while(root >= 0):
        heap_adjust(arr,root,n-1)
        root -= 1

    """去除大顶堆后，数据进行调整"""
    #掐掉堆顶后调整堆
    i = n - 1
    while(i >= 0):
        (arr[0],arr[i])=(arr[i],arr[0])
        heap_adjust(arr,0,i-1)
        i -= 1
    return arr

if __name__ == '__main__':
    arr = [1, 2, 3412, 121, 13, 23, 10]
    print(heap_sort(arr))