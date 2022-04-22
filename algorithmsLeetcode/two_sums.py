def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    j = -1
    for i in range(length):
        if target - nums[i] in nums:
            if (nums.count(target - nums[i])) == 1 & (target - nums[i] == nums[i]):
                continue
            else:
                """确认出错的原因在哪里,我观察到是没有及时跳出循环"""
                j = nums.index(target - nums[i], i + 1)
                break
    if j > 0:
       return [i, j]
    else:
       return []
if __name__ == '__main__':
    nums = [1,23,3,43,5]
    target = 4
    print(twoSum(nums,target))