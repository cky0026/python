def fun_draw(str):
    lines = len(str) - 1
    str_list = list(str)
    for i in range(lines, 0, -1):
        temp = str_list
        temp.insert(i, ' ')
        result = ''.join(temp)
        print(result)
        del temp[i]

    print("-" * (len(str) + 1))

    for i in range(1, lines + 1):
        temp = str_list
        temp.insert(i, ' ')
        result = ''.join(temp)
        print(result)
        del temp[i]


if __name__ == "__main__":
    str = input("Enter a string: ")
    fun_draw(str)
