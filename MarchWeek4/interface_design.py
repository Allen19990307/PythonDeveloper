import turtle
# 设置绘制的图形， fd代表移动的距离，right代表着转的角度
def square(t):
    print(t)
    # t.mainloop()
    for i in range(120):
        t.fd(10)
        t.right(3)

if __name__ == '__main__':
   t = turtle.Turtle()
   square(t)
