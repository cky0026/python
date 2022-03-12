l_days = ['日','一','二','三','四','五','六']
l_temp = [7]
sum = 0.0;
for num in range(0,7):  # 迭代 1 到 7 之间的数字
  print("请输入星期"+l_days[num]+"平均温度（摄氏度）：")
  n = float(input())
  sum += n;
  l_temp.append(n)

avg = 0.0;
avg = sum/7
str = "本周的平均气温（精确小数点后两位）是%.2f摄氏度" % (avg)
print(str)
