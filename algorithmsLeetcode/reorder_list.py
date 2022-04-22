# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# head = [1,2,3,4]
# Output: [1,4,2,3]
"""通过数组的解法"""
head = [0]
n = len(head)
Output = [ 0 for x in range(0,n)]
for i in range(0,n):
    if i % 2 == 0:
        Output[i] = head[i // 2]
    else:
        Output[i] = head[n-1 - (i//2)]
print(Output)
"""通过ListNode的解题方法"""









