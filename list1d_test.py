# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 10:53:55 2025

@author: DFSH
"""

scores = [59, 65, 70, 40, 100, 70] # 串列 python list

print('for-i loop')
# for-i loop
for i in range(len(scores)):
    if scores[i] >= 60:        
        print(i, '學生及格了')
    else:
        print(i, '學生被當掉了')

print('for-each loop')
# for-each loop        
for score in scores:
    if score >= 60:        
        print(score, '學生及格了')
    else:
        print(score, '學生被當掉了')

print('for-i-each loop')
# 
for i, score in enumerate(scores):
    if score >= 60:        
        print(i, score, '學生及格了')
    else:
        print(i, score, '學生被當掉了')
    