def fun_similar(strs):
    dict1 = count(strs[0])
    dict2 = count(strs[1])
    if dict1 == dict2:
        return True
    else:
        return False


def count(str):
    dic = {}
    for istr in str:
        if istr in dic:
            dic[istr] += 1
        else:
            dic[istr] = 1
    return dic


if __name__ == "__main__":
    while True:
        strs = input("请输入2个英文单词，以空格分隔: ").split()
        if fun_similar(strs):
            print("单词" + strs[0] + "和单词" + strs[1] + "是相似词！")
        else:
            print("单词" + strs[0] + "和单词" + strs[1] + "不是相似词！")
