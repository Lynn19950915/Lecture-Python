# Exercise 10: 情境實例 (2)

'''
10-1 數軸分段問題：
(1) Input : 日期資訊 (西元年、月份及日期)
    Output: 輸入日期為該年度之第幾天
'''

year=int(input("輸入西元年："))
month=int(input("請輸入月份："))
date=int(input("請輸入日期："))
day=0
norm=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 閏年規則：逢四則閏、逢百不閏、逢四百再閏
if year%4!=0:
    print("%d 年為平年"%(year))
# 4 的倍數為平年：必整除 100 而不整除 400
elif year%100==0 and year%400!=0:
    print("%d 年為平年"%(year))
else:
    norm[1]=29
    print("%d 年為閏年"%(year))

# 月份為 N，僅需累加至 N-1 月，即第 N-2 項
for i in range(0, month-1):
    day+=norm[i]
day+=date
print("%d/%d 是 %d 年的第 %d 天"%(month, date, year, day))

'''
(2) 公司對績效分數之規定：15 件 (含) 以下者，每案累積 1 點，25 件 (含) 以下者，高出部分每案累積 2 點
    30 件 (含) 以下者，高出部分每案累積 3 點，超出 30 件之部分，每案累積 5 點
    Input : 完成案件數
    Output: 顯示可獲得的績效分數
'''

case=int(input("請輸入完成案件數："))
# 數軸分段，case 將與下一項比較，列表需多寫末項 (必定小於而跳出迴圈)
caselist=[0, 15, 25, 30, case+1]
pointlist=[1, 2, 3, 5]
point=0

for i in range(len(caselist)):
    # 若超過該區段，可獲得該段所有點數
    if case>=caselist[i+1]:
        point+=(caselist[i+1]-caselist[i])*pointlist[i]
    # 若未超過該區段，則結算本段之點數，結束迴圈
    else:
        point+=(case-caselist[i])*pointlist[i]
        break

print("完案數 %d，可獲得績效 %d 點"%(case, point))

'''
10-2 獼猴桃問題：
已知一獼猴習慣每天丟棄一顆桃，再吃掉剩餘的一半
(1) Input : 剩下最後一顆桃的日數
    Output: 獼猴第一天擁有的桃子數
'''

day=int(input("請輸入獼猴吃桃日數："))
peach=0
list=[]

if day>=1:
    for i in range(0, day):
        # 前一天桃數=當天桃數 x2+1
        peach=2*peach+1
        list.append(peach)
    # 推算首日桃數，即反序輸出 list 末項
    print("獼猴第一天擁有 %d 顆桃子"%(list[-1]))
else:
    print("輸入有誤")

'''
(2) 五隻猴子在分桃，先丟棄一顆後取走餘下的五分之一，再交由下位重複執行
    最後所有猴子均取走整數顆桃。試求：桃數至少為何？
'''

# 取完後剩下五分之四，倒算可知：原先桃數=取後桃數 x1.25+1
peach=1
monkey=1
trys=1

# 第 n 隻猴子執行工作，當五隻均成功時即輸出
while monkey<6:
    if int(1.25*trys)==1.25*trys:
        trys=1.25*trys+1
        monkey+=1
    else:
        # 每當分桃失敗，peach 往下累計而猴子清零
        peach+=1
        monkey=1
        # peach 紀錄當前累積值，trys 負責於迴圈計算
        trys=peach

print("桃數至少為 %d"%(trys))

'''
10-3 報數問題：
設有 n 人圍圈報數，凡報至 3 者退出圈外並重新報數
Input : 參加人數
Output: 最終留下者，在第一輪是第若干個報數
'''

number=int(input("請輸入總人數："))
list=[]
for i in range(number):
    list.append(i+1)

# 想像成有無限張椅子，凡坐到 3 倍數就淘汰，否則就接續排到最末
n=1
while len(list)>1:
    if n%3!=0:
        list.insert(len(list), list.pop(0))
    else:
        list.pop(0)
    # n 會不斷遞增，維持 3 汰 1
    n+=1=
# 列表剩單一元素時終止並輸出
print(list[0])
