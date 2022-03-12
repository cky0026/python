import random

l = []
for i in range(0, 20):
    temp = random.randint(0, 100)
    l.append(temp)
print("初始列表为:", l)

for i in range(len(l) - 1, -1, -1):
    if l[i] % 2 == 1:
        del l[i]

print("最后列表为:", l)
