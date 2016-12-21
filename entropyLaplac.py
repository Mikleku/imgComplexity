import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import random
import math


def laplacEntr(fileList):
    entropyList =[]
    for file in fileList:
        img = cv2.imread(file,0)
        pixHSL = cv2.Laplacian(img,cv2.CV_64F)
        width = img.size[0]  
        height = img.size[1] 

        
         #entropy
        diff=0;
        arr_size=256*2-1
        prb=[0 for i in range(arr_size)]
        for i in range(width-1):
            for j in range(height):
                diff = pixHSL[i+1, j][2] - pixHSL[i, j][2]   
                if diff < (arr_size+1)/2 and diff > -(arr_size+1)/2:
                    prb[diff+(arr_size-1)//2] += 1         


        n=sum(prb)
        e=0
        for i in range(arr_size-1):
            prb[i] /= n
            if prb[i] != 0:
                e -= prb[i]*math.log(prb[i])
        e /=math.log(2)
        entropyList.append(e/8)
    return entropyList    
