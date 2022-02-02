import threading
import os,time
#线程模块的引入
def my_task1(name,message):
    print('What defines %s?'%name)
    print(message)

def my_task2(name,message):
    print('What decides %s?'%name)
    print(message)

T1 = threading.Thread(target=my_task1,args=('Young Men','Personality'))
T2 = threading.Thread(target=my_task2,args=('Old Men','Obedience'))
T1.start()
T2.start()