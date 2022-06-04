# 给定一个二叉树的根节点root ，返回它的中序遍历 。
#
# 示例
# 1：
# 输入：root = [1, null, 2, 3]
# 输出：[1, 3, 2]
#
# 示例
# 2：
# 输入：root = []
# 输出：[]
#
# 示例
# 3：
# 输入：root = [1]
# 输出：[1]
#
# 提示：树中节点数目在范围[0, 100]内-100 <= Node.val <= 100
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
from pyasn1.compat.octets import null
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None  # 指向该节点的左叶子节点
        self.right = None  # 指向该节点的右叶子节点

class Tree:
    def __init__(self):  # 构建一棵空树
        self.root = None  # 永远指向二叉树中的根节点

    def insert(self, item):  # 添加节点
        node = Node(item)
        # 如果是个空树
        if self.root is None:
            self.root = node
            return

        # 如果树不是空树
        cur = self.root
        q = [cur]  # 将根节点放入列表中
        while True:
            n = q.pop(0)  # 取出列表中的节点判断它的左右两个子节点是否为空
            if n.left is not None:
                q.append(n.left)  # 如果左子节点不为空就把它当做下一个主节点放入列表中
            else:
                n.left = node  # 如果左子节点为空就把加入的新节点插入
                break

            if n.right is not None:
                q.append(n.right)  # 同上判断右节点
            else:
                n.right = node
                break

    def travel(self):  # 查看所有节点
         cur = self.root
         q = [cur]

         while q:
             n = q.pop(0)
             print(n.item)
             if n.left is not None:
                 q.append(n.left)
             if n.right is not None:
                 q.append(n.right)

    def in_order(self,root):
       if root is None:
           return
       self.in_order(root.left)
       print(root.item)
       self.in_order(root.right)


if __name__ == '__main__':
    tree = Tree()
    tree.insert(1)
    tree.insert(null)
    tree.insert(2)
    tree.insert(3)
    # tree.travel()
    tree.in_order(tree.root)
