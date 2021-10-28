# Exercise 05: 基本操作：其他

'''
5-1 字典之生成：
(1) Input : 使用者自由輸入字典內容 (鍵-值對)
    Output: 輸出整本字典
'''

dict={}
while True:
    key=input("請輸入 key：")
    value=input("請輸入 value：")
    # 指定字典中之 key 對應 value
    dict[key]=value

    question=input("是否繼續輸入？ (Y/N)：")
    if question in("Y", "y"):
        continue
    elif question in("N", "n"):
        break
print(dict)

'''
(2) Input : 使用者自由輸入字典內容 (鍵-值對)
    Output: 將列表轉換為字典並輸出
'''

key_list=[]
value_list=[]
while True:
    key=input("請輸入 key：")
    value=input("請輸入 value：")
    key_list.append(key)
    value_list.append(value)

    question=input("是否繼續輸入？ (Y/N)：")
    if question in ("Y", "y"):
        continue
    elif question in ("N", "n"):
        break
# 以 dict 方法合併列表的對應項並輸出 (注意 dict 並非字典名稱)
print(dict([key_list, value_list]))

'''
5-2 字典之取值：
Input : 使用者自由輸入字典內容 (鍵-值對)
Output: 輸出值最大、最小之項目
'''

key_list=[]
value_list=[]
while True:
    key=input("請輸入 key：")
    value=float(input("請輸入 value："))
    key_list.append(key)
    value_list.append(value)

    question=input("是否繼續輸入？ (Y/N)：")
    if question in ("Y", "y"):
        continue
    elif question in ("N", "n"):
        break

# 字典無法逆推，可從對應位置 (index) 取 list
maximum=value_list.index(max(value_list))
minimum=value_list.index(min(value_list))
# 無須創建字典，只要仿製格式列印即可
print("最大值： {%s:%d}"%(key_list[maximum], value_list[maximum]))
print("最小值： {%s:%d}"%(key_list[minimum], value_list[minimum]))

'''
5-3 檔案之讀寫：
(1) Input : 使用者逐行輸入內容，直至鍵入 # 符號
    Output: 開一檔案路徑，將輸入字串轉為大寫後儲入文檔
'''

fileName=input("請輸入檔名：")
# 開啟檔案，設定路徑與讀寫格式
file1=open("C:/***/%s.txt"%(fileName), "w")

text=input("請輸入內容：")
while "#" not in text:
    file1.write(text.upper()+"\n")
    text=input("請繼續輸入內容：")
file1.close()

'''
(2) Input : 使用者於兩檔案自由輸入各一行字符
    Output: 開一檔案路徑，讀取兩檔案並依字母順序合併後儲入文檔
'''

context=[]
# 迴圈建立兩檔案
for i in range(0, 2):
    file=input("請輸入檔名：")
    with open("C:/***/%s.txt"%(file), "w") as w:
        text=input("請輸入內容：")
        w.write(text)
        w.close()
    # w 寫入、r 讀出，以 list 取項方式逐字符寫入列表，以利字母排序
    with open("C:/***/%s.txt"%(file), "r") as r:
        for item in list(r.read()):
            context.append(item)
        r.close()

context.sort()
file=input("請輸入合併檔名：")
with open("C:/***/%s.txt"%(file), "w") as w:
    # write 只適用字串，需取出列表項寫入
    for item in context:
        w.write(item)
    w.close()
