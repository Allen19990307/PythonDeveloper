"""python中的实际操作函数
   在python中调试实际错误的时候，问题可能不是在它本身
"""
import math
import time
def fermat_last_theorem(a,b,c,n):
    if a**n + b**n == c**n:
        print('fermat is wrong')
    else:
        print('fermat is right.')
if __name__ == '__main__':
    """计算信噪比"""
    # signal_power = 9
    # noise_power = 10
    # ratio = signal_power / noise_power
    # decibels = 10 * math.log10(ratio)
    # print(decibels)
    """输入函数的测试"""
    # s = input('what you want to do?\n')
    # s1 = "love is the reason and answer for everthing."
    # print(s)
    """时间函数的转换操作"""
    f = time.time()
    local_time = time.localtime(f)
    strftime = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print(strftime)
    """验证费马大定理"""
    fermat_last_theorem(1,2,23,4)
