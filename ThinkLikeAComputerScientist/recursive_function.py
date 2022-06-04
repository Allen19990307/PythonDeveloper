"""实现一个简单的递归函数：
   传话筒，将话筒传到第一排，然后再传回来
"""
def countdown(n):
    if n <= 0:
        print("You have no score left.")
    else:
        print(n)
        countdown(n-1)

def print_n(s,n): 
    if n <= 0:
        print("Game is over.")
    else:
        print(s+str(n-1))
        print_n(s,n-1)
if __name__ == '__main__':
    # countdown(3)
    print_n('企业家的故事',3)