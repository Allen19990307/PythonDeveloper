
"""have a heart to be number one"""
def insert_sort(arr):
    count = len(arr)
    for i in range(1,count):
        key = i - 1
        mark = arr[i]
        while key >= 0 and arr[key] > mark :
            arr[key + 1] = arr[key]
            key -= 1
        arr[key+1] = mark
    return  arr

if __name__ == '__main__':
    nums = [5, 2, 3, 1]
    nums2 = [5, 1, 1, 2, 0, 0]
    sort = insert_sort(nums)
    print(sort)