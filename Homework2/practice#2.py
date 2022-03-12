import random

print("(1)")
l =[]
for i in range(0,13):
 temp = random.randint(0,100)
 l.append(temp)
print("初始列表为:",l)

l1 = l[0:6]
l2= l[6:]
l1.sort(reverse=False)
l2.sort(reverse=True)
temp_l = l1+l2
print("排序操作得到的列表为:",temp_l)

print("(2)")
print("初始列表为:",l)
print("切片操作得到的列表为:",l[::3])
