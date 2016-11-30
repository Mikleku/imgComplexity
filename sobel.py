import random
import math
from PIL import Image, ImageDraw
image = Image.open("1.jpg") 
imageHSL= image.convert("HSV")
draw = ImageDraw.Draw(image)   
drawHSL = ImageDraw.Draw(imageHSL) 
width = image.size[0]  
height = image.size[1]  
pix = image.load()
pixHSL=imageHSL.load()

  
for i in range(1,width-1):
    for j in range(1,height-1):
        a=pixHSL[i,j][0]
        b=pixHSL[i,j][2]
        x=pixHSL[i-1,j+1][2]+2*pixHSL[i,j+1][2]+pixHSL[i+1,j+1][2] - ( pixHSL[i-1,j-1][2]+2*pixHSL[i,j-1][2]+pixHSL[i+1,j-1][2])
        y=pixHSL[i-1,j-1][2]+2*pixHSL[i-1,j][2]+pixHSL[i-1,j+1][2] - ( pixHSL[i+1,j-1][2]+2*pixHSL[i+1,j][2]+pixHSL[i+1,j+1][2])
        G=abs(x)+abs(y)
        drawHSL.point((i, j), (a,0,int(G)))

imageHSL= imageHSL.convert("RGB")
imageHSL.save("ans1.jpg", "JPEG")
del drawHSL
