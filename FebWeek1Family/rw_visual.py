import matplotlib.pyplot as plt
from random_walk import RandomWalk
"""使用随机模拟的方式"""
# 创建一个RandomWalk实例类
# while True:
#     # 调用其填充方法
#     rw = RandomWalk()
#     rw.fill_walk()
#     # 选择经典的颜色填充的方式，根据时间的先后进行颜色的填充
#     plt.style.use('classic')
#     fig, ax = plt.subplots(figsize = (16,9))
#     point_numbers = range(rw.num_points)
#     ax.plot(rw.x_values,rw.y_values,c = point_numbers,
#                cmap = plt.cm.Blues, edgecolors= 'none',s = 15)
#     # 突出起点和终点
#     ax.plot(0,0,c = 'green',edgecolors = 'none',s = 100)
#     ax.plot(rw.x_values[-1],rw.y_values[-1],c = 'red',edgecolors = 'none' ,s = 100)
#     # 隐藏坐标轴的方式
#     ax.get_xaxis().set_visible(False)
#     # ax.get_yaxis().set_visible(False)
#     plt.show()
#     keep_running = input("Make another walk? (Y/N): ")
#     if keep_running =='N':
#         break

#刻画布朗的分子无规则运动路线
while True:
    # 调用其填充方法
    rw = RandomWalk()
    rw.fill_walk()
    # 选择经典的颜色填充的方式，根据时间的先后进行颜色的填充
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (16,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values,rw.y_values,color = 'green',linewidth = 0.5)
    # 突出起点和终点
    ax.plot(0,0,color = 'green',linewidth = 0.5)
    # 隐藏坐标轴的方式
    ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (Y/N): ")
    if keep_running =='N':
        break

