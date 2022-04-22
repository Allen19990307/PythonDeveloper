# Example
# 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1]
# has
# the
# largest
# sum = 6
#
# Example
# 2:
# Input: nums = [1]
# Output: 1
#
# Example
# 3:
# Input: nums = [5, 4, -1, 7, 8]
# Output: 23

# 单个的枚举叠加
from typing import List

# nums = [5, 4, -100, 1, 2]
# length = len(nums)
# max = 0
# for i in range(0,length):
#     if max + nums[i] > max:
#         max = 0
#         for i in range(0,i+1):
#             max += nums[i]
# print(max)

# 最大数组的统计:如何理解动态规划？
def maxSubArray(nums:List[int])->int:
    length = len(nums)
    if length == 0:
        return 0
    """为每个值的赋予0"""
    dp = [0 for _ in range(length)]
    dp[0] = nums[0]
    for i in range(1,length):
        if dp[i - 1] >= 0:
            dp[i] = dp[i - 1]+nums[i]
        else:
            dp[i] = nums[i]
    return max(dp)
if __name__ == '__main__':
    nums = [5, 4, -100, 1, 2]
    print(maxSubArray(nums))
