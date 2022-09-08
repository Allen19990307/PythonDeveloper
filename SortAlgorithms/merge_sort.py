"""归并排序"""
def merge(s1,left,mid,right):
    """归并排序的设置，左右边界的确认"""
    l = mid - left + 1
    r = right - mid

    l_list = [0] * l
    r_list = [0] * r

    for i in range(l):
        l_list[i] = s1[left + i]
    for j in range(r):
        r_list[j] = s1[mid + 1 + j]

    i = 0
    j = 0
    k = left
    while i < l and j < r:
        if l_list[i] < r_list[j]:
            s1[k] = l_list[i]
            i = i + 1
        else:
            s1[k] = r_list[j]
            j = j + 1
        k = k + 1
    while i < l:
        s1[k] = l_list[i]
        i = i + 1
        k = k + 1
    while j < r:
        s1[k] = r_list[j]
        j = j + 1
        k = k + 1

def merge_sort(s1,left,right):
    if left < right:
        mid =  (left + (right - 1)) // 2
        merge_sort(s1,left,mid)
        merge_sort(s1,mid + 1,right)
        merge(s1,left,mid,right)

if __name__ == '__main__':
    s1 = [2,1341,41,3,123,1232,42,43,1245]
    lens = len(s1)
    merge_sort(s1, 0, lens-1)
    print(s1)
