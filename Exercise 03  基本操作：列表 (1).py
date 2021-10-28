# Exercise 03: 基本操作：列表 (1)

'''
3-1 列表之生成：
(1) Input : 使用者自由輸入列表之項 (直至不繼續輸入)
    Output: 將列表逆序輸出顯示
'''

list=[]
while True:
    text=input("請輸入內容：")
    list.append(text)
    question=input("是否繼續輸入？ (Y/N)：")
    # 以 tuple 或 list 定義有效輸入值均可 (類似 SQL 語法)
    if question in("Y", "y"):
        continue
    elif question in("N", "n"):
        break
    else:
        print("輸入有誤")
print(list[::-1])

'''
(2) Input : 使用者自由輸入列表之項 (直至不繼續輸入)
    Output: 將列表排序後，由大至小逐項輸出
'''

list=[]
while True:
    # 要做排序，需將輸入由字串轉為數字
    number=float(input("請輸入數字："))
    list.append(number)
    question=input("是否繼續輸入？ (Y/N)：")
    # 以 tuple 或 list 定義有效輸入值均可 (類似 SQL 語法)
    if question in("Y", "y"):
        continue
    elif question in("N", "n"):
        break
    else:
        print("輸入有誤")
list.sort()
for item in list[::-1]:
    print(item)

'''
3-2 列表之排序：
Input : 已有一排序好列表，使用者自由輸入一數字
Output: 將數字加入列表後，重新排序輸出
'''

list=[9, 22, 23, 34, 100]
number=float(input("請輸入數字："))

list.append(number)
# 方法呼叫，不可直接寫入 print (會顯示 None)
list.sort()
print(list)

'''
3-3 列表之串接：
Input : 已有一排序好列表，使用者自由輸入串接符
Output: 將列表各項以串接符連接後，輸出顯示
'''

list=[10, 4, 19, 11, 21]
concat=input("請輸入串接符：")

# 串接條件為字符，即各項需為 str
for i in range(len(list)):
    # 搭配 index 才能轉換列表項，for item in list 無法對列表本身影響
    list[i]=str(list[i])
print(concat.join(list))

'''
3-4 列表項之移動：
(1) Input : 使用者自由輸入列表之項 (直至不繼續輸入)
    Output: 將最大項與首項、最小項與末項交換後輸出列表
'''

list=[]
while True:
    number=float(input("請輸入一數字："))
    list.append(number)
    question=input("是否繼續輸入？ (Y/N)：")
    if question in ("Y", "y"):
        continue
    elif question in ("N", "n"):
        break

# 結合 index 與 max 函數取得項數位置
max_index=list.index(max(list))
list[0], list[max_index]=list[max_index], list[0]
# 交換可能影響最小項位置，要再重新取值 (重要)
min_index=list.index(min(list))
list[-1], list[min_index]=list[min_index], list[-1]
print(list)

'''
(2) Input : 使用者自由輸入列表之項 (直至不繼續輸入)，並指定由後移動項數
    Output: 將該項數移至列表之首，之後輸出結果
'''

list=[]
# 列表內移動會覆蓋取代，故將變化寫於一新表
newlist=[]
while True:
    number=float(input("請輸入一數字："))
    list.append(number)
    question=input("是否繼續輸入？ (Y/N)：")
    if question in ("Y", "y"):
        continue
    elif question in ("N", "n"):
        break
index=int(input("將後面幾項移至前面："))

# 從倒數 n 項 (list[-n]) 逐序新增至 list[-1]
for i in range(index):
    newlist.append(list[-index+i])
# 從首項 list[0] 逐序新增至 list[len-n-1]
for j in range(len(list)-index):
    newlist.append(list[j])
print(newlist)
