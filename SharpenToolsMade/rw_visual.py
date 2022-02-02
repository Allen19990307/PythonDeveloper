import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个RandomWalk实例类
rw =  RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values,rw.y_values,s = 15)
plt.show()