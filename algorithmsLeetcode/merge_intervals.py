# Given an array
# of intervals
# where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            """列表为空或者当前区间与上一区间不重合，直接添加"""
            # print(merged[-1][1])
            merged.append(interval)
        else:
            """否则的话，我们就可以和上一区间进行合并"""
            merged[-1][1] = max(merged[-1][1],interval[1])
    return merged
# 实现最小的范例
if __name__ == '__main__':
    s1 = [[1,5],[6,12],[8,78]]
    """结束的末端小于当前的开头，则赋予新的值"""
    # for i in s1 :
    #     print(i[0])
    print(merge_intervals(s1))

