# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 10:36:07 2025

@author: DFSH
"""

height = int(input('請輸入身高(cm): '))
weight= int(input('請輸入體重(kg): '))

height = height / 100
height = height ** 2
bmi = weight / height

if bmi >= 27:
    print("啊～「肥胖」，需要立刻力行「健康體重管理」囉！")
elif bmi >= 24:
    print("「體重過重」了，要小心囉，趕快力行「健康體重管理」！")
elif bmi >= 18.5:
    print("恭喜！「健康體重」，要繼續保持！")
else:
    print("「體重過輕」，需要多運動，均衡飲食，以增加體能，維持健康！")
    