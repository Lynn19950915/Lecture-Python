# Exercise 01: 基本操作：數值

'''
1-1 數值之比較：
(1) Input : 使用者自由輸入兩個數字
    Output: 顯示數字一大、小或等於數字二
'''

# input 預設為字串，需轉為 int 型態
# 使用者可能輸入小數：float 搭配 %s 輸出
number1=float(input("請輸入數字一："))
number2=float(input("請輸入數字二："))

if number1>number2:
    # 格式化輸出，等同 number1, ">", number2
    print("%s>%s"%(number1, number2))
elif number1==number2:
    print("%s=%s"%(number1, number2))
else:
    print("%s<%s"%(number1, number2))

'''
(2) Input : 使用者自由輸入學期成績
    Output: 顯示成績之轉換等第 (90 分以上 A、80 分以上 B、70 分以上 C、餘則為 F)
'''

# 使用者可能輸入小數：float 搭配 %s 輸出
grade=float(input("請輸入學期成績："))

if grade>=90:
    print("%s 分，等第 A"%(grade))
elif grade>=80:
    print("%s 分，等第 B"%(grade))
elif grade>=70:
    print("%s 分，等第 C"%(grade))
else:
    print("%s 分，等第 F"%(grade))

'''
1-2 數值之排序：
(1) Input : 使用者自由輸入兩個數字
    Output: 將兩變數之值互換後輸出
'''

number1=float(input("請輸入 x 之值："))
number2=float(input("請輸入 y 之值："))

print("x=%.1f, y=%.1f"%(number2, number1))

'''
(2) Input : 使用者自由輸入三個數字
    Output: 由小而大輸出使用者給定之三數字
'''

list=[]
number1=int(input("請輸入整數一："))
number2=int(input("請輸入整數二："))
number3=int(input("請輸入整數三："))

list.append(number1)
list.append(number2)
list.append(number3)
list.sort()
# 若要由大而小輸出，則 list[::-1]
print(list)

'''
(3) Input : 使用者決定輸入數量，並輸入數字
    Output: 由大而小輸出使用者給定之所有數字
'''

list=[]
amounts=int(input("你想輸入幾個數字："))
# 迴圈：使用者 input、list 隨後寫入
for i in range(1, amounts+1):
    number=int(input("請輸入整數 %s："%(i)))
    list.append(number)

list.sort()
print(list[::-1])

'''
1-3 階和、階乘運算：
(1) Input : 使用者自由輸入一個正整數
    Output: 顯示該數字之階和 (1+2+...+n)
'''

number=int(input("請輸入一個正整數："))
sum=0

# 設計迴圈：range 含頭不含尾
for i in range(1, number+1):
    sum+=i
print("1 加到 %d 之和 = %d"%(number, sum))

'''
(2) Input : 使用者自由輸入一個正整數
    Output: 顯示該數字之階乘 (1x2+...xn)
'''

number=int(input("請輸入一個正整數："))
multiple=1

for i in range(1, number+1):
    multiple*=i
print("1 乘到 %d 之積 = %d"%(number, multiple))

'''
(3) Input : 使用者自由輸入一個正整數
    Output: 顯示該數字之階乘之和(1!+2!+...+n!)
'''

number=int(input("請輸入一個正整數："))
sum=0
multiple=1

for i in range(1, number+1):
    # 階乘：算到幾往上乘到幾
    multiple*=i
    # 階乘之和：每輪結束前將結果累加
    sum+=multiple
print("1 到 %d 的階乘和 = %d"%(number, sum))
