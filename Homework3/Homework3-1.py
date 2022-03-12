print('请输入一组整数：')
str = '['+input()+']'
l = eval(str)
result = []

sl = set(l)
for i in sl:
    if l.count(i) > 1:
        result.append(i)
print('得到新的列表为：',result)


