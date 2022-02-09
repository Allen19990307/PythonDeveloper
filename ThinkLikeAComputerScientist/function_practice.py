import math
"""基本的函数调用"""
print(int(-2.3))
"""信噪比的计算"""
singal_power = 5
noise_power = 10
ratio = singal_power / noise_power
ratio_ = 10 * math.log10(ratio)
print(ratio_)
"""正弦函数的计算"""
radians = 0.8
height = math.sin(radians)
print(height)
# 计算正弦值,这边计算的结果为什么和2的平方根一半是相同的？
degree = 45
radians = degree / 180.0 * math.pi
sin = math.sin(radians)
print(sin)

f = math.sqrt(2) / 2.0
print(f)