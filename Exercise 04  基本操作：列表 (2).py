# Exercise 04: 基本操作：列表 (2)

'''
4-1 巢狀列表之輸出：
Input : 使用者自由輸入學生姓名、座號及成績 (直至不繼續輸入)
Output: 以學生為單位，輸出逐項資料
'''

list=[]
# 逐筆增寫巢狀列表，以 index 作為位置取項
index=0
while True:
    list.append([])
    name=input("請輸入學生姓名：")
    stuid=input("請輸入學生座號：")
    score=float(input("請輸入學生成績："))

    # 巢狀列表：取項後可於項內再新增值
    list[index].append(name)
    list[index].append(stuid)
    list[index].append(score)
    index+=1

    question=input("是否繼續輸入？ (Y/N)：")
    if question in ("Y", "y"):
        continue
    elif question in ("N", "n"):
        break
    else:
        print("輸入有誤")
        break
for record in list:
    print(record)

'''
4-2 矩陣之生成：
(1) Input : 使用者自由輸入方陣層數，並依序填入
    Output: 輸出生成之方陣
'''

level=int(input("要輸入幾層方陣："))
matrix=[]
# 逐筆增寫巢狀列表，以 index 作為位置取項
index=0
for i in range(0, level):
    matrix.append([])
    # 方陣：控制行列數量相同
    for j in range(0, level):
        value=float(input("請輸入 (%d, %d) 矩陣值："%(i, j)))
        matrix[index].append(value)
    # 迴圈結束後調整 index (往下寫第 n+1 層)
    index+=1
# 逐層輸出，n 層即輸出 n 行
for item in matrix:
    print(item)

'''
(2) Input : 使用者自由輸入方陣層數，並依序填入
    Output: 計算方陣主對角線之元素總和
'''

level=int(input("要輸入幾層方陣："))
matrix=[]
# 逐筆增寫巢狀列表，以 index 作為位置取項
index=0
sum=0
for i in range(0, level):
    matrix.append([])
    # 方陣：控制行列數量相同
    for j in range(0, level):
        value=float(input("請輸入 (%d, %d) 矩陣值："%(i, j)))
        matrix[index].append(value)
    # 累加對角線 (i=j) 值總和
    sum+=matrix[index][index]
    index+=1

print("主對角線之元素總和為：%.1f"%(sum))

'''
★ 4-3 矩陣之運算：
Input : 使用者自由輸入方陣層數，並依序填入 (兩個方陣)
Output: 雙方陣於對應位置相加運算，輸出結果方陣
'''

level=int(input("要輸入幾層方陣："))
sum_matrix=[]

# 兩次迴圈供輸入雙方陣
for i in range(0, 2):
    # 初始：將矩陣清空、填位歸零
    matrix=[]
    index=0
    for j in range(0, level):
        matrix.append([])
        # 方陣：控制行列數量相同
        for k in range(0, level):
            value=float(input("請輸入 (%d, %d) 矩陣 %d 值："%(j, k, i+1)))
            matrix[index].append(value)
        index+=1

    sum_matrix.append(matrix)
# 將 sum_matrix 兩項中對應的位置相加，並覆蓋於首項
for l in range(0, level):
    for m in range(0, level):
        sum_matrix[0][l][m]=sum_matrix[0][l][m]+sum_matrix[1][l][m]
for item in sum_matrix[0]:
    print(item)
