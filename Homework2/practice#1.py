print("请输入列表元素个数：")
n = int(input())
print("请输入列表元素的起始下标start：")
start = int(input())
print("请输入列表元素的结束下标end：")
end = int(input())
l = list(range(0, n * 2, 2))
print("初始列表为:",l)
print("切片操作得到的列表为:",l[start:end +1])
