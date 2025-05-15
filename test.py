# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 08:21:46 2025

@author: 林學億
@school: 龍華科技大學, 資訊網路工程系
"""

score = 50

"""
80-100: A
60-79: B
40-59: C
<=39: D
"""

# if score >= 40:
#     print("C")
# elif score >= 60:
#     print("B")
# elif score >= 80:
#     print("A")
# else:
#     print("D")

if score >= 80:
    print("A")
elif score >= 60:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")

# if score >= 60:
#     print('及格了')
# else:
#     print('被當掉了')




# for i in range(10):
#     print(i)
# print()

# for i in range(2, 10):
#     print(i)
# print()

# for i in range(2, 10, 3):
#     print(i)
# print()



# 版本 4
# str_in = input('請輸入一個數字：')

# y = int(str_in) # 
# n = len(str(y))
# for i in range(n):
#     temp = (y // (pow(10, i))) % 10
#     print('第', i, '位數為', temp)


"""
# 版本 3
str_in = input('請輸入一個數字：')

y = int(str_in) # 假設 y 一定是 6 位數
n = len(str(y))
i = 0
while i<n:
    temp = (y // (pow(10, i))) % 10
    print('第', i, '位數為', temp)
    i = i + 1
"""

"""
# 版本 2
i = 0 # 第 i 位數(i = 0, 1, 2, ....)
while y > 0:
    temp = y % 10 # 踢掉最低位數
    print("第", i, "位數為", temp)
    i=i+1
"""

"""
# 版本 1
y0 = y % 10 # 抓取最低位數

y = y // 10 # 踢掉最低位數
y1 = y % 10 # 抓取最低位數

y = y // 10 # 踢掉最低位數
y2 = y % 10 # 抓取最低位數

y = y // 10 # 踢掉最低位數
y3 = y % 10 # 抓取最低位數

y = y // 10 # 踢掉最低位數
y4 = y % 10 # 抓取最低位數

y = y // 10 # 踢掉最低位數
"""

