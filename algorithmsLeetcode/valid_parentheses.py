# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# 实现思路： 判断是否是对称的表达框
# 使用栈,将元素压进栈内，随后再一个个弹出进行匹配
# 1.栈的数据结构  2.弹出匹配  3. if [ then ]  引入标志符号的功能
class Stack(object):
    #对栈实现初始化的功能
    def __init__(self):
        self.items = []
    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []
    #返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]
    # 返回栈的大小
    def size(self):
        return len(self.items)
    # 入栈
    def push(self,item):
        self.items.append(item)
    # 出栈
    def pop(self):
        return self.items.pop()

def Valid_Parentheses(s1):
    flag = True
    if(s1 == ']'):
        flag = True
        print(flag)
    else:
        flag = False
        print(flag)


if __name__ == '__main__':
    s1 = "[]{}"
    num_len = len(s1)
    # flag = True
    stack = Stack()
    for i in s1:
        stack.push(i)
    Valid_Parentheses(stack.pop())

