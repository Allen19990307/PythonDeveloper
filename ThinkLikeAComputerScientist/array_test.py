from numpy import array

s = array([[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
  [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])

print(s[1][4])

l = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(l[3])

temp = [('a', 1, 1.5),
        ('b', 2, 5.1),
        ('c', 9, 4.3)]

temp.sort(key = lambda x:x[0]!='c')

findindex = lambda self,i,value:sorted(self,key=lambda x:x[i]!=value)[0]

print(findindex(temp,0,'a'))