def func(str):
    uppers = 0
    lowers = 0
    digits = 0
    others = 0
    dict = {}

    for istr in str:
        if istr.isupper():
            uppers += 1
        elif istr.islower():
            lowers += 1
        elif istr.isdigit():
            digits += 1
        else:
            others += 1
    else:
        dict.setdefault('大写字母', uppers)
        dict.setdefault('小写字母', lowers)
        dict.setdefault('数字', digits)
        dict.setdefault('其他字符', others)
    return dict

if __name__=="__main__":
    str = input("请输入一个字符串: ")
    print(func(str))
