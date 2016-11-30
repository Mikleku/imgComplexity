import  dirScan
from  laplac_countLine import laplac
from entropy import entropy
from velvet import velvet
path='./pics'
masks = ['.jpg','.jpeg','.JPG','.JPEG','.png','.PNG']

fileList=dirScan.fileList(path,masks)
a=entropy(fileList)
b=laplac(fileList)
for i in range( len(fileList)):
    print(fileList[i])
    print("E=" + str(round(a[i],3)))
    print("L=" + str(round(b[i],3)))
    print()
    
  



#velvet(fileList)
