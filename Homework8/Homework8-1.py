import re

text = '''
    1.   abc  2016-10-31  
    2.   xyz   2016-9-4
    3.   aef   2016-10-aa
    4.    asasf asdf 10-14
    5.  2013-10-3  234234
    6.  1945-8-15 abc  1945
    7.  1972-01-30 asdf  1988-10-1
'''
arr = text.split('.')
list = []
for i in range(1,len(arr)):
    temp = arr[i].split()
    j = 0
    #print(temp)
    while(j < len(temp)):
        temp1 = re.match(r"(\d{4}-\d{1,2}-\d{1,2})", temp[j])
        if (temp1 != None):
            list.append(temp1.string)
        j=j+1;

print("将文本里出现的合法日期转换格式：")
for i in range(0, len(list)):
    temp = list[i].split('-')
    str1 = str(i+1) +". "+temp[2].zfill(2)+"/"+temp[1].zfill(2)+"/"+temp[0]
    print(str1)



