import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = cv2.imread('oshawott.jpg')

kernel_detecting_borders = np.array([[-1, -1, -1], 
                                     [-1, 8, -1], 
                                     [-1, -1, -1]])
kernel_blur = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]]) / 9

def applying_kernel(img, kernel):
    
    height, width = img.shape[:2]
    new_img = np.zeros_like(img, dtype=float)
    
    for cc in range(3):
        for i in range(height - 2):
            for j in range(width - 2):
                for m in range(3):
                    for n in range(3):
                        new_img[i][j][cc] += img[i+m][j+n][cc] * kernel[m][n]

    return np.clip(new_img, 0, 255).astype(np.uint8)

new_img = applying_kernel(img, kernel_detecting_borders)
new_img2 = applying_kernel(img, kernel_blur)

cv2.imshow('Original', img)
cv2.imshow('Detecting Borders', new_img)
cv2.imshow('Blur', new_img2)

cv2.waitKey()
cv2.destroyAllWindows()
