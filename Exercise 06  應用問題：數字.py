# Exercise 06: 應用問題：數字

'''
6-1 字牌問題：
(1) 今有無限多 0~7 號牌
    Input : 欲組成幾位數
    Output: 顯示可組成若干種之奇數
'''

digit=int(input("請輸入數字位數："))
if digit==1:
    # 末位必為1, 3, 5, 7
    amounts=4
elif digit>1:
    # 除一位數外，首位均為 7 種、中間無限制 (8 種)
    amounts=7*8**(digit-2)*4
else:
    # 非正整數直接終止，不需印出 amounts
    print("輸入錯誤")
    exit()
print(amounts)

'''
(2) 今有無限多 1~4 號牌
    顯示可組成若干種三位數，又其中各位數均異者有多少
'''

list1=[]
list2=[]

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            # 各位數可重複，直接寫入列表一
            list1.append(100*i+10*j+k)
            if i!=j and j!=k and k!=i:
                # 符合各位數均異者，寫入列表二
                list2.append(100*i+10*j+k)

print("可組成 %d 種三位數"%(len(list1)))
print("其中各位數均異者共有 %d 種"%(len(list2)))

'''
6-2 水仙花數問題：
水仙花數之定義：各位數的三次方總和，等同自身之數
試列出所有三位數中，滿足條件之水仙花數
'''

for number in range(100, 1000):
    # 分解逐位數：取整數除法，相當於取高斯 (gauss)
    i=number//100
    j=(number-i*100)//10
    k=number-i*100-j*10

    if i**3+j**3+k**3==number:
        print("%d 是水仙花數"%(number))

'''
6-3 位數分解：
(1) Input : 任一正整數
    Output: a.該數字為幾位數，並逐位輸出
            b.判斷該數字是否為回文數或水仙花數
'''

number=int(input("請輸入一正整數："))
# 位數分解：轉為字串，逐字元寫入列表
numlist=list(str(number))
sum=0

print("%d 是 %d 位數"%(number, len(str(number))))
for item in numlist:
    print(item)
    sum+=int(item)**3

if numlist==numlist[::-1]:
    print("%d 是回文數"%(number))
else:
    print("%d 不是回文數"%(number))
if sum==number:
    print("%d 是水仙花數"%(number))
else:
    print("%d 不是水仙花數"%(number))

'''
(2) Input : 任一正整數，及所欲取之位數範圍 (由左數來第 n~m 位)
    Output: 顯示位數範圍內之所有數字
'''

number=int(input("請輸入一正整數："))
index_n=int(input("從左數來第幾位取值："))
index_m=int(input("取到從左數來第幾位："))

if index_n<=index_m:
    # 取 n~m 位，在位置上即為 n-1~m-1
    for digits in range(index_n-1, index_m):
        # 轉為字串並逐字元寫入列表，取項
        print(list(str(number))[digits])
else:
    print("輸入有誤")

'''
6-4 位數謎題：
已知一個二位數 c 滿足：8*c 為二位數、9*c 為三位數、809*c 為四位數
試求出：符合條件之二位數 c，以及 809*c 之運算結果
'''

for c in range(10, 100):
    if 8*c in range(10, 100) and 9*c in range(100, 1000) and 809*c in range(1000, 10000):
        print("二位數 c=%d"%(c))
        print("%d=809x%d"%(809*c, c))

'''
6-5 平方數問題：
(1) Input : 任一個正數
    Output: 該輸入數之平方，若運算後小於 50 則終止
'''

number=float(input("請輸入一正數："))
while True:
    # 需同時滿足二者才可繼續迴圈
    while number>=0 and number**2>=50:
        # 允許一位之小數輸出　　　
        print("%.1f 之平方數為 %.1f"%(number, number**2))
        number=float(input("請繼續輸入數字："))

    # 兩種例外狀況之結果：重新開始 (continue)、結束 (break)
    if number<0:
        print("輸入錯誤，請重新輸入")
        number=float(input("請重新輸入一正數："))
        continue
    elif number>=0 and number**2<50:
        print("%.1f 之平方數為 %.1f，遊戲終止"%(number, number**2))
        break

'''
(2) Input : 任一非負整數
    Output: 判斷該數是否為完全平方數
'''

number=int(input("請輸入非負整數："))
square=[]

# 生成平方數列表 (注意：0, 1 均滿足)，範圍直到該數為止
for item in range(0, number+1):
    square.append(item**2)

if number>=0:
    if number in square:
        print("%d 是完全平方數"%(number))
    else:
        print("%d 不是完全平方數"%(number))
else:
    print("輸入有誤")
