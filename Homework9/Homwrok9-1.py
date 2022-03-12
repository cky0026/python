import re


def main():
    text = open("address-7.txt", "r")
    dict = {}
    names = []
    for line in text:
        addresses = []
        if "<name>" in line:
            name = (line.replace("<name>", "")).replace("</name>", "")
            if name:
                names.append(name)
        if "@" in line:
            tempText = line.split(" ")
            i = 0
            while(i < len(tempText)):
                address = re.match(r'[\w.-]+@[\w.-]+', tempText[i])
                if address:
                    addresses.append(tempText[i])
                    dict[tempText[i]] = name
                i= i+1

    names = sorted(names,key= lambda i:i[0])
    print(names)
    print('-'*30)
    print("每个人的email地址如下：")
    n = 0
    while(n < len(names)):
        print(str(n+1)+"."+names[n].strip('\n')+":")
        for index in dict:
            if dict[index] == names[n]:
                print("     ",index.strip('\n'))
        n = n+1
    print('-' * 30)
if __name__ == "__main__":
    main()
