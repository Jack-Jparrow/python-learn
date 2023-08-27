TempStr=input("")
if TempStr [-1] in ['F','f']:
    c=(eval(TempStr[0:-1])-32)/1.8
    print("{:.2f}c".format(c))
elif TempStr [-1] in ['C','c']:
    f=32+eval(TempStr[0:-1])*1.8
    print("{:.2f}f".format(f))
else:
    print("error")
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
def tempConvert(ValueStr):
    if ValueStr[-1] in ['f','F']:
        c=(eval(ValueStr[0:-1])-32)/1.8
        print("{:.2f}c".format(c))
    elif ValueStr[-1] in ['c','C']:
        f=1.8*eval(ValueStr[0:-1])+32
        print("{:.2f}f".format(f))
    else:
        print("error")
TempStr=input("")
tempConvert(TempStr)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from turtle import*
color("red")
pensize(15)
fd(200)
seth(120)
fd(200)
seth(-120)
fd(200)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from turtle import*
setup(650,450,200,200)
penup()
fd(-250)
pendown()
pensize(25)
color("purple")
seth(-40)
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(16,180)
fd(40*2/3)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from turtle import*
def drawsnake(rad,angle,len,neckrad):
    for i in range(len):
        circle(rad,angle)
        circle(-rad,angle)
    circle(rad,angle/2)
    fd(rad)
    circle(neckrad+1,180)
    fd(rad*2/3)
def main():
    setup(1300,800,0,0)
    pythonsize=30
    pensize(pythonsize)
    color("blue")
    seth(-40)
    drawsnake(40,80,5,pythonsize/2)
main()
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
