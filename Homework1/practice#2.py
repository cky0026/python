print("请您输入华氏度：")
f = float(input())
c = (5 / 9) * (f - 32)

for i in range(0,40):
 print('*',end='')
print("")

str1 = "%.*f 华氏度" % (1,f)
str2 = "转变成摄氏度为 %.*f" % (2,c)
print(str1+str2)

for i in range(0,40):
 print('*',end='')