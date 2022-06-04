import time
"""test personal computer performance"""
def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product
def testSpeed():
    start_time = time.time()
    prod = calcProd()
    endTime = time.time()
    print('The result is %s digits  long.' % len(str(prod)))
    print('took %s seconds to run' %(endTime-start_time))
if __name__ == '__main__':
    testSpeed()
    print(time.ctime())
