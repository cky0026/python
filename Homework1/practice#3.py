import random

n = random.randint(0,10000)
str1 = "随机产生一个0到10000之间的整数为： %d" %(n)
print(str1)
for i in range(0,20):
 print('*-',end='')
print("")

a = int(n/10000)
b = int(n/1000) - a*10
c = int(n/100) - a*100 -b*10
d = int(n/10) - a*1000 -b*100 - c*10
e = n - a*10000 -b*1000 - c*100 - d*10

m = a+b+c+d+e
str2 = "%d的各个数字之和 = %d "%(n,m)
print(str2)
for i in range(0,20):
 print('*-',end='')
print("")