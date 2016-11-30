import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread('1.jpg',0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobel = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

 
result = Image.fromarray(laplacian)
#result = Image.fromarray(sobel)

laplacian = result.load()
width = result.size[0]  
height = result.size[1]  
s=0

for i in range(width):
    for j in range(height):
         if laplacian[i,j]>0:
             s += 1   

print(s/(width*height))
result.convert('RGB').save("ans1.jpeg")


