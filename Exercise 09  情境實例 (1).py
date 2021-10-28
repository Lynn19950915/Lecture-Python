# Exercise 09: 情境實例 (1)

'''
9-1 密碼轉譯器：
公司密碼規則為：將四位數密碼均加上 5 後，將首尾兩項對調，再將中間的兩項對調
Input : 加密後之四位數
Output: 回算出原始密碼
'''

password=input("請輸入加密後密碼：")
# 以字串逐位倒序輸出，再轉數字計算
for item in list(password)[::-1]:
    item=int(item)-5
    print(item, end="")

'''
9-2 九九乘法表：
參考輸出：https://pic.pimg.tw/dodo02/1532186567-158506301.png
'''

# 橫向輸出，所以 range(1,10) 寫在外迴圈
for n in range(1, 10):
    for m in range(2, 6):
        # %2d：利用位數對齊，不換行加 space
        print("%dx%d=%2d"%(m, n, m*n), end=" ")
    # 都乘完 n 後才換行
    print("")

print("")
for n in range(1, 10):
    for m in range(6, 10):
        print("%dx%d=%2d"%(m, n, m*n), end=" ")
    print("")

'''
9-3 彈跳球問題：
已知球體在落地後，反彈的高度會是原高度的一半
Input : 起始落下高度、反跳次數
Output: a.球體第 n 次落地後所經之總路徑長
        b.球體第 n 次反彈的高度
'''

height=float(input("請輸入起始高度："))
rebounce=int(input("請輸入反跳次數："))
route=height

if rebounce>=1:
    for i in range(1, rebounce):
        # 第 n 次落地，路徑長就累加前一次反彈高度 (來回乘上 2)
        route+=2*0.5**(rebounce-1)*height
    # 反彈 n 次，高度即指數減半
    rebounce_height=0.5**(rebounce)*height

    print("第 %d 次落地後所經之總路徑長：%.1f"%(rebounce, route))
    print("第 %d 次反彈的高度：%.1f"%(rebounce, rebounce_height))
else:
    print("輸入有誤")

'''
9-4 猜數字遊戲：
Input : 設定一 1~100 之密碼，使用者自由輸值猜測
Output: 提供範圍提示，並顯示總猜測次數
'''

import random
# 產生隨機值：設定均質分布並轉成整數
bingo=int(random.uniform(0.5, 100.5))
times=0

while True:
    guess=int(input("請輸入一個數字 (1~100)："))
    times+=1
    if guess<bingo:
        print("比 %d 再大一點，猜第 %d 次:"%(guess, times+1))
    elif guess>bingo:
        print("比 %d 再小一點，猜第 %d 次:"%(guess, times+1))
    else:
        print("Bingo! 答案就是 %d"%(guess))
        break

if times<5:
    print("你花了 %d 次，非常厲害！"%(times))
elif times < 9:
    print("你花了 %d 次，還不錯喔～"%(times))
else:
    print("你花了 %d 次，再接再厲！"%(times))

'''
9-5 整除生產器：
Input : 使用者自由輸入一正奇數
Output: 顯示最少幾個 9 才能整除該數 (例：999999/13=76923)
'''

number=int(input("請輸入一正奇數："))
digit=1

while True:
    # 迴圈設定：10^N-1
    if (10**digit-1)%number==0:
        break
    else:
        digit+=1
print("%d/%d=%d"%(10**digit-1, number, (10**digit-1)/number))
