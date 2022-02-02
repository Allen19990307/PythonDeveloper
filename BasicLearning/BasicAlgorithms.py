class Solution(object):
    def find__left__repeat__num(self,nums):
        res = []
        for i in range(len(nums)):
            find = -1
            for j in range(i):
                if nums[j] == nums[i]:
                    find = j
                    break
            res.append(find)
        return res

if __name__ == '__main__':
    s1 = [1,3,1,2,1]
    print(s1)
    a = Solution()
    print(a.find__left__repeat__num(s1))