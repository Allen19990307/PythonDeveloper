class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self,root:TreeNode) -> TreeNode:
        # 递归的结束条件
        if not root:
            return  None
        #递归交换当前节点的左右子树
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
if __name__ == '__main__':
    node = TreeNode()
    node.val = 3
    node.left = 12
    node.right = 13
    solution = Solution()
    tree = solution.invertTree(node)
    print(tree)