from plotly.graph_objs import Bar, Layout
from plotly.offline import offline

from die import Die
die_1 = Die()
die_2 = Die()
"""创造results的参数列表，使用列表解析，简化代码量"""
results = [die_1.roll() * die_2.roll() for i in range(1000)]

"""结果的数据分析,每个点数出现的可能性为多少"""
max_sides = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(1,max_sides + 1)]
"""结果的可视化处理"""
x_values = list(range(1,max_sides + 1))
data = [Bar(x = x_values,y = frequencies)]

"""先看中文的需求，然后再去书写"""
x_axis_config = {'title': 'result','dtick':1}
y_axis_config = {'title':'frequency'}
my_layout = Layout(title='投掷两个D6 1000次的结果', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')

