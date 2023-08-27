#coding:utf-8
import os  
import sys  
import os.path  
import shutil  
  
#获取当前路径  
def fileDir() :  
    path = sys.path[ 0 ]  
    print(path)  
    #判断为脚本文件还是编译后文件，如果是脚本文件则返回脚本目录，否则返回编译后的文件路径  
    if os.path.isdir( path ) :  
        return path  
    elif os.path.isfile( path ) :  
        return os.path.dirname( path )  
  
#获取文件后缀名  
def suffix( file, *suffixName ) :  
    array = map( file.endswith, suffixName )  
    if True in array :  
        return True  
    else :  
        return False  
  
#删除目录下扩展名为.o,.exe,.bak的文件  
def deleteFile() :  
    targetDir = fileDir()  
    for file in os.listdir( targetDir ) :  
        targetFile = os.path.join( targetDir, file )  
        if suffix( file, '.avi', '.bak', '.exe' ):  
            os.remove( targetFile )  
  
if __name__ == '__main__' :  
    deleteFile()  
