import os

def fileList(userDir,masks):
    fileList=[]
    files=os.listdir(path=userDir) 
    #masks = ['.jpg','.jpeg','.JPG','.JPEG','.png','.PNG']
    for file in files:
        for m in masks:
            if file.find(m)!=-1:
                fileList.append(userDir+'/'+file)
    return fileList                
