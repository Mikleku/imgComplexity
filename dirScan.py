import os
import shutil 

def fileList(userDir,masks): #получает список изображений в папке
    fileList=[]
    files=os.listdir(path=userDir) 
    #masks = ['.jpg','.jpeg','.JPG','.JPEG','.png','.PNG']
    for file in files:
        for m in masks:
            if file.find(m)!=-1:                
                fileList.append(userDir+'/'+file)
    return fileList                
 
def getStructure(userDir):
    files=os.listdir(path=userDir)
    
    
    
def createStructure(userDir,masks):
    dirList=[]
    startDir=os.getcwd() 
    os.chdir(userDir)
    files=os.listdir() 
    for file in files:
        for m in masks:
            if file.find(m)!=-1:
                dirName=file[:file.rindex('.')] #без расширения
                if files.count(dirName)!=0:
                    shutil.rmtree(dirName)
                os.makedirs(dirName)
                shutil.copy(file, dirName+'/'+file )
                dirList.append(userDir+'/'+dirName)
    os.chdir(startDir)
    
    return dirList                
 
