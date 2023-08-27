textFile=open("71.txt","rt")
print(textFile.readline())
textFile.close()
binFile=open("71.txt","rb")
print(binFile.readline())
binFile.close()
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
fname=input("请输入要打开的文件：")
fo=open(fname,"r")
for line in fo.readlines():
    print(line)
fo.close()
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
fname=input("请输入要打开的文件：")
fo=open(fname,"r")
for line in fo:
    print(line)
fo.close()
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
fname=input("请输入要写入的文件：")
fo=open(fname,"w+")
ls=["唐诗","宋词","元曲"]
fo.writelines(ls)
for line in fo:
    print(line)
fo.close()
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from PIL import Image
im=Image.open('timg.gif')
try:
    im.save('picfame{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save('picframe{:02d}.png'.format(im.tell()))
except:
    print("处理结束")