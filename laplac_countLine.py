import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def laplac(fileList):
    sobelList=[]
    for file in fileList:
        img = cv2.imread(file,0)
        laplacian = cv2.Laplacian(img,cv2.CV_64F)

        result = Image.fromarray(laplacian)
        laplacian = result.load()
        width = result.size[0]  
        height = result.size[1]  
        s=0

        for i in range(width):
            for j in range(height):
                 if laplacian[i,j]>0:
                     s += 1   
        sobelList.append(s/(width*height))
    return sobelList   
        #print(s/(width*height))
        #result.convert('RGB').save("ans1.jpeg")


