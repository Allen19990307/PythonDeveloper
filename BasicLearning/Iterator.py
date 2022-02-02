#迭代器是从常规可迭代对象转换过来的
I_data = ['Allen','Love','Coding','&','Basketball']
new_data = iter(I_data)
# print(next(new_data))
# print(next(new_data))
# print(next(new_data))
# print(next(new_data))
# print(next(new_data))

print("---------------------------------------------")
#测试for循环下的可迭代对象 和迭代器之间的不同表现
print("可迭代对象")
for i in I_data:
    print(i)
for i in I_data:
    print(i)

print("可迭代器")
for i in new_data:
    print(i)
for i in new_data:
    print(i)
print("----------------------------------------")
#怎样声明使用一个生成器？
#简单生成器
def practice_skills():
    yield 'Target'
    yield 'Focus'
    yield 'Feedback'
    yield 'Correct'
#注意缩进  indnext(my_learn)ent
my_learn = practice_skills()
print(next(my_learn))
print(next(my_learn))
print(next(my_learn))
print(next(my_learn))

print("---------------------------------------")
def breakthrough_logic():
    n=['极度渴望','脚踏实地','突破舒适圈的勇气']
    for i in n:
      yield i
my_way = breakthrough_logic()
print(next(my_way))
print(next(my_way))
print(next(my_way))

#how to declare and  transfer constructors?
def hello():
    print('No.1')
    return 'Finish'
    print('Who know?')
print(hello())

def gen_num():
    n = 0
    while True:
        yield n
        n = n+1
        print('从0到1的过程')
my_num = gen_num()
print(next(my_num))

# 总结：return 有类似与break，但此处结束，但我们可以观察到其有返回结果。
#      yield生成器的标志之一，使用的时候返回结果，返回上次记录的位置


