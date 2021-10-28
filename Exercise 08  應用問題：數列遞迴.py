# Exercise 08: 應用問題：數列遞迴

'''
8-1 遞迴求算：
已知遞迴式 S=a+aa+aaa+...
Input : a 代表的數字，以及加總項數 n
Output: n 項遞迴之加總結果 S
'''

number=int(input("請輸入 a 代表之數字 (1~9)："))
digits=int(input("請輸入總運算項數 n："))
S=0
list=[]

# 逐位數各自相加，例：8x1、7x10...
for n in range(0, digits):
    S+=number*10**(n)*(digits-n)
    # 字串相乘 = 相同數字輸出
    list.append(str(number)*(n+1))
# 2+22+222+2222=2468
print("+".join(list)+"=%d"%(S))

'''
8-2 費氏數列：
Input : 項數 (n>1)
Output: 截至該項數之費氏數列
'''

number=int(input("請輸入欲觀察之項數："))
# 費氏數列前兩項為 1
list=[1, 1]

if number==1:
    print(list[0])
elif number>1:
    #自第三項起，數值均為前兩項之和
    for i in range(2, number):
        next=list[i-2]+list[i-1]
        list.append(next)
    print(list)
else:
    print("輸入有誤")

'''
8-3 雙重費氏數列：
(1) 已知一數列分子、分母均為費氏數列 (分子首兩項為 2, 3、分母則為 1, 2)
    Input : 項數 (n>1)
    Output: 前 n 項之數列內容
'''

number=int(input("請輸入欲觀察之項數："))
# 由首二項推衍餘項，需先定義於列表
list1=[2, 3]
list2=[1, 2]

if number>=2:
    for item in range(2, number):
        i=list1[item-2]+list1[item-1]
        j=list2[item-2]+list2[item-1]
        list1.append(i)
        list2.append(j)

division=[]
# 位置比項數少 1 (range0)
for i in range(number):
    division.append(list1[i]/list2[i])
print(division)

'''
(2) Input : 任一正整數
    Output: 當輸入值 n 為奇數，輸出 S=1/1+1/3+1/5+...+1/n
                        偶數，輸出 S=1/2+1/4+1/6+...+1/n
'''

number=int(input("請輸入一正整數："))
sum=0

if number%2==0:
    # 數列項數為 number/2 (起項= 2、末項= n)
    for i in range(1, int(number/2)+1):
        sum+=1/(2*i)
else:
    # 數列項數為 number/2 (範圍 +1、總和 -1)
    for j in range(1, int((number+1)/2)+1):
        sum+=1/(2*j-1)
print(sum)

'''
8-4 圖樣輸出：
(1) Input : 三角形之腰長 (n>1)
    Output: 輸出等腰三角形
'''

level=int(input("請輸入三角形之腰長："))
for i in range(1, level+1):
    print("# "*i)

'''
(2) Input : 菱形之層數 (n>1)
    Output: 輸出菱形
'''

level=int(input("請輸入菱形之層數："))
# 遞增迴圈
for i in range(1, level+1):
    # 空格逐行減少 (至第 n 層為 0)，字符則逐行增加 2
    print(" "*(level-i)+"#"*(2*i-1))
# 遞減迴圈
for j in range(1, level):
    # 空格逐行增加，字符則逐行減少 (至第 n-1 層為 1)
    print(" "*j+"#"*(2*level-1-2*j))

'''
(3) Input : 正方形之階數 (n>1)
    Output: 輸出正方形
'''

level=int(input("請輸入正方形之階數："))
print("# "*level)
for i in range(level - 2):
    # 中間行只要印出首尾即可 (空心正方形)
    print("#"+" "*(2*level-3)+"#")
print("# "*level)

'''
★ 8-5 三角數列：
(1) Input : 數列三角形之階數 (n>1)
    Output: 輸出數列三角形
'''

level=int(input("請輸入三角形之階數："))
list=[]
for i in range(1, level+1):
    # 逐次新增一個列表項
    list.append([])
    for j in range(1, level+1):
        # (巢狀) 列表第 n 項會有 n 個值
        if i>=j:
            list[i-1].append(j)

for item in list:
    print(item)

'''
(2) Input : 楊輝三角形之階數 (n>1)
    Output: 輸出楊輝三角形
'''

level=int(input("請輸入三角形之階數："))
list=[]
for i in range(1, level+1):
    list.append([])
    for j in range(1, level+1):
        # (巢狀) 列表第 n 項會有 n 個值，先填入 1
        if i>=j:
            list[i-1].append(1)

# 第 n 階是由第 n-1 階相加得來
for i in range(1, level-1):
    for j in range(1, level-1):
        # 注意：巢狀列表相加之項數
        if i>=j:
            list[i+1][j]=list[i][j-1]+list[i][j]

#以列表逐項輸出
for i in range(1, level+1):
    print(list[i-1])
#列表中巢狀取值，逐值輸出
for i in range(1, level+1):
    for item in list[i-1]:
        print(item, end=" ")
    print("")
