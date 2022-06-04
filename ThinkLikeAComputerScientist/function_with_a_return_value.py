import math
# exp = math.exp(1.0)

"""返回值"""
def area(radius):
    return math.pi * radius ** 2
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
# print(str(area(2))+'返回值的应用'+str(absolute_value(-1))+'compare'+str(compare(1,21)))

"""6.2 增量开发"""
def distance(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    # print('dx is',dx)
    # print('dy is',dy)
    # print(dsquared)
    print('两点之间的距离是:'+str(result))
    return result
# distance(1,2,4,6)

"""6.3 组合：计算圆心和圆上任意一点的距离"""
def circle_area(rx,ry,x1,y1):
    radius = distance(rx, ry, x1, y1)
    result = area(radius)
    return result
print(circle_area(1,2,4,6))

"""6.4 布尔函数"""
def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False
def is_between(x,y,z):
    if x <= y and y <= z:
        return True
    else:
        return False
print(is_between(1,2,1.5))









