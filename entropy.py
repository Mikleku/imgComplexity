import random
import math
from PIL import Image, ImageDraw
import os

def entropy(fileList):
    entropyList=[]
    for file in fileList:
        print(file)
        image = Image.open(file) 
        imageHSL= image.convert("HSV")
        drawHSL = ImageDraw.Draw(imageHSL) 
        width = image.size[0]  
        height = image.size[1]  
        pixHSL=imageHSL.load()


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
        entropyList.append(e)
    return entropyList    

