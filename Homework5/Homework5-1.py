print("Please input a positive integer less than 1000：")
n = int(input())
while n <= 0 or n > 1000:
    print("Please input valid value：")
    n = int(input())
final = n
flag = 1
l = []
temp = 2
while flag == 1:
    if n == 1:
        break;
    if n % temp == 0:
        n = n // temp
        l.append(temp)
    else:
        temp += 1

print(final, "=", end="")
print("*".join(str(i) for i in l))
