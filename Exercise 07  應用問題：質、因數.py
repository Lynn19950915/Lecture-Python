# Exercise 07: 應用問題：質、因數

'''
7-1 因數問題：
(1) Input : 任一正整數
    Output: a.該數共有若干因數，包含哪些數
            b.判斷該數是否為質數
'''

number=int(input("請輸入一正整數："))
factorlist=[]

# 因數：上下界必為 1 與自己 (質數也只有這兩個)
for factor in range(1, number+1):
    if number%factor==0:
        factorlist.append(factor)

print("%d 共有 %d 個因數，包含："%(number, len(factorlist)), factorlist)
if len(factorlist)==2:
    print("%d 為質數"%(number))
else:
    print("%d 不是質數"%(number))

'''
(2) 完全數之定義：所有因數 (不含自己) 之總和等同該數者
    Input : 任一位數
    Output: a.所有該位數之因數分解結果 (例：二位數 10~99)
            b.該位數中所有符合條件之完全數
'''

digit=int(input("請輸入檢驗位數："))
# 以列表收集所有符合之數字
perfect_number=[]

for number in range(10**(digit-1), 10**digit):
    factorlist=[]
    sum=0

    # 完全數不算自己，上界保持為 number
    for factor in range(1, number):
        if number%factor==0:
            factorlist.append(factor)
    # 加總所有因數並檢驗
    for item in factorlist:
        sum+=item
    if sum==number:
        perfect_number.append(number)
    # 逐數輸出：所有因數列表
    print(number, factorlist)

print("%d 位數之完全數共有 %d 個，包含："%(digit, len(perfect_number)), perfect_number)

'''
7-2 質數問題：
(1) Input : 任一正整數 (n>1)
    Output: 判斷該數是否為質數
'''

number=int(input("請輸入一正整數 (n>1)："))
factorlist=[]

if number>1:
    # 避開 1 和自身，故質數會找不到任何因數
    for factor in range(2, number):
        if number%factor==0:
            factorlist.append(factor)

    if len(factorlist)==0:
        print("%d 為質數"%(number))
    else:
        print("%d 不是質數"%(number))
else:
    print("輸入有誤")

'''
(2) Input : 任一數字範圍 (上、下界)
    Output: a.該範圍內共有若干質數，又 b.其中最大、最小者為何
'''

lower=int(input("請輸入下界範圍："))
upper=int(input("請輸入上界範圍："))
# 以列表收集所有符合之質數
prime_number=[]

for number in range(lower, upper+1):
    factorlist=[]
    for factor in range(2, number):
        if number%factor==0:
            factorlist.append(factor)
    if len(factorlist)==0:
        prime_number.append(number)

print("在 %d~%d 範圍之內，共有 %d 個質數"%(lower, upper, len(prime_number)))
# 依序輸出 (最小、最大者分別為首項及末項)
print("其中最小者為 %d，最大者為 %d"%(prime_number[0], prime_number[-1]))

'''
★ 7-3 質因數問題：
Input : 任一正整數 (n>1)
Output: a.該數之所有質因數
        b.該數之質因數分解結果 (例：90=2*3*3*5)
'''

integer=int(input("請輸入一正整數 (n>1)："))

# 以列表收集所有小於該數的質數
prime_number=[]
for number in range(2, integer):
    factorlist=[]
    for factor in range(2, number):
        if number%factor==0:
            factorlist.append(factor)
    if len(factorlist)==0:
        prime_number.append(number)

prime_factorlist1=[]
# 不可重複：用 for 迴圈逐一檢之
for item in prime_number:
    if integer%item==0:
        prime_factorlist1.append(item)
print("%d 之質因數包含："%(integer), prime_factorlist1)

prime_factorlist2=[]
i=0
division=integer
# 可以連除：由 while 迴圈條件判定
while i<len(prime_factorlist1):
    if division%prime_factorlist1[i]==0:
        prime_factorlist2.append(prime_factorlist1[i])
        division/=prime_factorlist1[i]
        # 無法整除才往下檢驗，否則持續相除
        continue
    else:
        i+=1

# 輸出 * 連接格式，需將列表項轉為字串
for j in range(len(prime_factorlist2)):
    prime_factorlist2[j]=str(prime_factorlist2[j])
print("%d="%(integer)+"*".join(prime_factorlist2))
