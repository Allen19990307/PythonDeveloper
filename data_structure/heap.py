# 实现堆
class Heap:
    def __init__(self,n,count):
        self.n = n
        self.count = count
        self.a = []
    def Heap(self,capacity):
        self.a = [capacity + 1]
        self.n = capacity
        self.count = 0
    def insert(self,data,n,count):
        if count >= n :
            return
        ++count
        self.a[count] = data
        i  = count
        while i // 2 and  self.a[i] > self.a[i // 2]:
            self.swap(self.a, i, i // 2)
            i = i // 2
    def  swap(self,a,i,j):
       temp = a[i]
       a[i] = a[j]
       a[j] = temp
if __name__ == '__main__':
   Heap

