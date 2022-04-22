import math
import turtle
""""""
def circle(t,r,angle):
    arc(t,r,angle)
def arc(t,r,angle):
    artc_length = int(2 * math.pi * r * angle // 360)
    n = artc_length // 3 + 1
    step_length = artc_length // n
    step_angle  = angle // n
    poly_line(t,n,step_length,step_angle)
def poly_line(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
if __name__ == '__main__':
    """new a object"""
    allen = turtle.Turtle()
    """draw it """
    circle(allen,5,360)
