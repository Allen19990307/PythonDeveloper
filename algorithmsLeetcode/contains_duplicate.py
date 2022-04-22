# 217.
# Example1:
# Input: nums = [1, 2, 3, 1]
# Output: true
# Example2:
# Input: nums = [1, 2, 3, 4]
# Output: false
# Example3:
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true
# 方式一： 采取双循环遍历的方式，进行判断是否重复
from typing import List
# nums = [1, 2, 3, 4, 1]
# len = len(nums)
# count = 0
# for i in range(0,len):
#     for j in range(i + 1,len):
#         if nums[i] == nums[j]:
#             print(str(i)+" "+str(j))
#             count = count + 1
#             break
# if count != 0:
#     print(count)
#     print("True")
# else:
#     print("False")

# 方式二:使用set的存储方式
def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 1]
    print(containsDuplicate(nums))




