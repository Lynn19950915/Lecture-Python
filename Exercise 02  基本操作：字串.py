# Exercise 02: 基本操作：字串

'''
2-1 字串之串接：
Input : 使用者自由輸入兩個字串
Output: 顯示兩字串之串接結果，以及總長度
'''

string1=input("請輸入字串一：")
string2=input("請輸入字串二：")

# (自動判斷) 字串相加即連接
output=string1+string2
print(output)
print("字串總長度為：%d"%(len(output)))

'''
2-2 字串之查找：
Input : 使用者自由輸入兩個字串
Output: 子字串是否出現於母字串 (Y/N)，若有，輸出首次出現之位置
'''

string1=input("請輸入母字串：")
string2=input("請輸入子字串：")

ncount=string1.count(string2)
if ncount>0:
    # find 可查找子字串之出現位置 (僅輸出首筆)
    print("有出現，首次出現位置為", string1.find(string2))
else:
    print("無出現")

'''
2-3 字串之排序：
(1) Input : 使用者自由輸入三個字串
    Output: 依字序輸出使用者給定之三字串
'''

list=[]
for i in range(1, 4):
    string=input("請輸入字串 %s："%(i))
    list.append(string)
list.sort()
print(list)

'''
(2) Input : 使用者決定輸入數量，並輸入字串
    Output: 依字序反向輸出使用者給定之所有字串
'''

list=[]
amounts=int(input("你想輸入幾個字串："))
for i in range(1, amounts+1):
    string=input("請輸入字串 %s："%(i))
    list.append(string)
list.sort()
print(list[::-1])

'''
2-4 字符之輸出：
Input : 使用者自由輸入一個字串
Output: 倒序輸出使用者輸入之字符 (例：apple 輸出 elppa)
'''

# 解一
string=input("請輸入字串：")
for item in list(string[::-1]):
    # 分行輸出: print(item)
    print(item, end="")

# 解二
string=input("請輸入字串：")
# 設定無分隔符，需搭配 str 型態列表
print("".join(list(string))[::-1])

'''
2-5 字符之辨析：
Input : 使用者自由輸出一個字串
Output: 顯示字串中包含多少英文、數字、空格與其他字符
'''

# 將字串轉為列表 (逐字符做分析)
stringlist=list(input("請輸入字串："))
letter=0
number=0
space=0
others=0

for item in stringlist:
    # 字串之方法，回傳 True/False
    if item.isalpha():
        letter+=1
    elif item.isdigit():
        number+=1
    elif item.isspace():
        space+=1
    else:
        others+=1
print("英文：%d，數字：%d，空格：%d，其他字符：%d"%(letter, number, space, others))

'''
2-6 字符之判斷：
Input : 使用者輸入英文星期之首個字母 (M, W, T...)
Output: 根據首字母輸出完整星期名，若無法判斷則繼續輸入次個字母
'''

first=input("請輸入星期之首字母：")

if first=="S" or first=="s":
    second=input("請繼續輸入星期之次字母：")
    if second=="A" or second=="a":
        print("星期六 Saturday")
    elif second=="U" or second=="u":
        print("星期天 Sunday")
    else:
        print("輸入有誤")

elif first=="T" or first=="t":
    second=input("請繼續輸入星期之次字母：")
    if second=="H" or second=="h":
        print("星期四 Thursday")
    elif second=="U" or second=="u":
        print("星期二 Tuesday")
    else:
        print("輸入有誤")

elif first=="F" or first=="f":
    print("星期五 Friday")
elif first=="M" or first=="m":
    print("星期一 Monday")
elif first=="W" or first=="w":
    print("星期三 Wednesday")
else:
    print("輸入有誤")
