import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def sobel(file):    
    img = cv2.imread(file,0)
    img = cv2.blur(img,(5,5))
    laplacian= cv2.Laplacian(img,cv2.CV_64F)
    result = Image.fromarray(laplacian)
    name=file[:file.rindex('.')]+"_laplac"+file[file.rindex('.'):]
    result.convert('RGB').save(name)
                               
   

def laplac(file):
    img = cv2.imread(file,0)
    img = cv2.blur(img,(5,5))
    sobel = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    result = Image.fromarray(sobel)
    name=file[:file.rindex('.')]+"_sobel"+file[file.rindex('.'):]
    result.convert('RGB').save(name)



 
