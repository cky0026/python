name=['Bob', 'Alan', 'Mandy', 'Rob']
score=[ 95.0,  86.0, 83.5,90.0]
a = dict()
for i in range(0,4):
	a[name[i]] = score[i]
print('字典a为：',a)

#平均成绩
temp = 0
l = len(a)  # 取字典中键值对的个数
s = sum(a.values())  # 取字典中键对应值的总和
average = s / l
print('平均成绩为：',average)

# 字典转换为列表
b = list(a.items())
print('得到的列表b为：',b)

