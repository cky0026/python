def func(num):
    if 0 < num < 100001:
        # 1当成特殊情况,从二位数开始
        print('1 =( 0 + 1 ) ** 2')
        for m in range(10, num+1):
            ostr = str(m)
            for n in range(1, len(ostr)):
                a = int(ostr[0:n])
                b = int(ostr[n:len(ostr)])
                if (a+b)**2 == m:
                    print(m, '=(', a, '+',b,') ** 2')
    else:
        print('输入不合法！')


if __name__=="__main__":
    num = int(input("请输入一个不大于100000的正整数: "))
    print(func(num))