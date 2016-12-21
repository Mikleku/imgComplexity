import  dirScan
from  laplac_countLine import laplac
from entropy import entropy
from entropyLaplac import laplacEntr
from velvet import velvet
import sobel_openCv as fil
import os

masks = ['.jpg','.jpeg','.JPG','.JPEG','.png','.PNG']

#список папок созданныx в катологе
path='./pics'
dirList=dirScan.createStructure(path,masks)

startDir=os.getcwd()

for item in dirList:
    print(item+"---------------------------")
    fileList=dirScan.fileList(item,masks)
    for i in fileList:
        fil.sobel(i)
        fil.laplac(i)
        
    fileList=dirScan.fileList(item,masks)    
    a=entropy(fileList)
    #b=laplac(fileList)
    #c=laplacEntr(fileList)
    for i in range(len(fileList)):
        print(fileList[i])
        print("E=" + str(round(a[i],3)))
        #print("L=" + str(round(b[i],3)))
        #print("E+L=" + str(round(c[i],3)))
        print()
    
  



#velvet(fileList)
