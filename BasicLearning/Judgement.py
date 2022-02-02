#判断语句   满足条件则if后输出  不然else后的语句输出
A_learn_mode = 'active'
if(A_learn_mode.__contains__('active')):print("Good for you")
else:
    print("Find your love!")
B_learn_mode = 'I do not know'
if(B_learn_mode.__contains__('active')):print("Good for you")
else:
    print("Find your love!")

#for
for name in A_learn_mode:
 print(name)
 #如果我们要打印5次active呢？
 # 接下来引入  range() 方法
 for i in range(5):
     print('I wanna be active to lead my life!!')


#while   注意缩进 indent   同一级别，开头对齐！！！
number  = 5
while number >= 0:
   print('点火倒计时：'+str(number))
   number = number-1
print('Take off!')
