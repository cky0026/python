print("Please input a positive integer less than 20：")
n = int(input())
final = n
while n <= 0 or n > 20:
    print("Please input valid value：")
    n = int(input())

#上半部分
for i in range(0,n+1):
    temp = 2*i -1
    temp2 = 2*n - i*2
    print(" "*temp2,temp * "* ")

#下半部分
for i in range(n-1,-1,-1):
    temp = 2 * i - 1
    temp2 = 2 * n - i*2
    print(" " * temp2, temp * "* ")
