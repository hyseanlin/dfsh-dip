import numpy as np
import cv2

img1 = np.zeros([480, 640], dtype='uint8') # unit8: only for range 0-255
img2 = np.zeros([480, 640], dtype='uint8')
cv2.imshow('My First Image', img1)

for i in range(256):
    img2show = img2.copy()
    img2show[70:100, i:i+30] = 255
    cv2.imshow('My Second Image', img2show)
    cv2.waitKey(10) # waitKey(0) 無窮等待，直到使用者按下任一鍵
    
cv2.destroyAllWindows()
