import  dirScan
from entropy import entropy
from velvet import velvet
path='./pics'
masks = ['.jpg','.jpeg','.JPG','.JPEG','.png','.PNG']

fileList=dirScan.fileList(path,masks)
print(entropy(fileList))

