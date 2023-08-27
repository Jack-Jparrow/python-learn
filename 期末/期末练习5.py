print("Happy birthday to you!")
print("Happy birthday to you!")
print("Happy birthday, dear Mike!")
print("Happy birthday to you!")
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
def happy():
    print("Happy birthday to you!")
def happyB(name):
    happy()
    happy()
    print("Happy birthday, dear {}".format(name))
    happy()
happyB("Mike")
print()
happyB("Lily")
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
def max(x,y):
    if x>y:
        return x
    else:
        return y
max(12,15)
print(max(12,max(16,5)))
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
f=lambda x,y:x+y
print(type(f))
f(10,12)
print(f)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
def add(x,y=0,z=1):
    s=x+y+z
    return s
ad=add(100)
print(ad)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
def vfunc(a,*b):
    print(type(b))
    for n in b:
        a +=n
    return a
vfunc(1,2,3,4,5)
print(vfunc)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
def func(a,b):
    return a*b
s=func("knock~",2)
print(s)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
def func(a,b):
    return(b,a)
s=func("knock~",2)
print(s,type(s))
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
n=1
def func(a,b):
    n=b
    return a*b
s=func("knock~",2)
print(s,n)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
n=1
def func(a,b):
    global n
    n=b
    return a*b
s=func("knock",2)
print(s,n)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
ls=[]
def func(a,b):
    ls.append(b)
    return a*b
s=func("knock~",2)
print(s,ls)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
ls=[]
def func(a,b):
    ls=[]
    ls.append(b)
    return a*b
s=func("knock~",2)
print(s,ls)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
a=1
def second():
    b=2+a
    def thirth():
        c=3+a
        d=4+b
        print(a,b,c,d)
    thirth()
    print(a,b)
second()
print(a)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
a=1
def second():
    a=2
    def thirth():
        a=3
        print("thirth_a:",a)
    thirth()
    print("second_a:",a)
second()
print("first_a:",a)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
a=1
def second():
    global a
    a=2
    def thirth():
        a=3
        print("thirth_a:",a)
    thirth()
    print("second_a:",a)
second()
print("first_a:",a)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
a=1
def second():
    a=2
    def thirth():
        global a
        a=3
        print("thirth_a:",a)
    thirth()
    print("second_a:",a)
second()
print("first_a:",a)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
a=1
def second():
    a=2
    def thirth():
        nonlocal a
        a=3
        def fourth():
            a=4
            print("fourth_a:",a)
        fourth()
        print("thirth_a:",a)
    thirth()
    print("second_a:",a)
second()
print("first_a:",a)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
a=1
def second():
    a=2
    def thirth():
        a=3
        def fourth():
            nonlocal a
            a=4
            print("fourth_a:",a)
        fourth()
        print("thirth_a:",a)
    thirth()
    print("second_a:",a)
second()
print("first_a:",a)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
a=[1,2,3,4,5]
print(a)
def square(x):
    for i ,j in enumerate(x):
        x[i]=j*j
square(a)
print(a)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from datetime import datetime
today=datetime.now()
print(today)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from datetime import datetime
today=datetime.utcnow()
print(today)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from datetime import datetime
someday=datetime(2016,9,16,22,33,32,7)
print(someday)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
someday=datetime(2016,9,16,22,33,32,7)
print(someday.isoformat())
print(someday.isoweekday())
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
print(someday.strftime("%Y-%m-%d %H:%M:&S"))
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from turtle import*
import datetime
def drawLine(draw):
    pendown() if draw else penup()
    fd(40)
    right(90)
def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9,] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    left(180)
    penup()
    fd(20)
def drawDate(date):
    for i in date:
        drawDigit(eval(i))
def main():
    setup(800,350,200,200)
    penup()
    fd(-300)
    pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y%m%d'))
    hideturtle()
main()
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from turtle import*
import datetime
def  drawGap():
    penup()
    fd(5)
def drawLine(draw):
    drawGap()
    pendown() if draw else penup()
    fd(40)
    drawGap()
    right(90)
def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    left(180)
    penup()
    fd(20)
def drawDate(date):
    pencolor("red")
    for i in date:
        if i =='-':
            write('年',font=("Arial",18,"normal"))
            pencolor("green")
            fd(40)
        elif i =='=':
            write('月',font=("Arial",18,"normal"))
            pencolor("blue")
            fd(40)
        elif i=='+':
            write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
def main():
    setup(800,350,200,200)
    penup()
    fd(-350)
    pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    hideturtle()
main()
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
def fact(n):
    if n ==0:
        return 1
    else:
        return n*fact(n-1)
num=eval(input("请输入一个整数："))
print(fact(abs(int(num))))
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from turtle import*
def koch(size,n):
    if n==0:
        fd(size)
    else:
        for angle in [0,60,-120,60]:
            left(angle)
            koch(size/3,n-1)
def main():
    setup(800,400)
    speed(0)
    penup()
    goto(-300,-50)
    pendown()
    pensize(2)
    koch(600,3)
    hideturtle()
main()
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from turtle import*
def koch(size,n):
    if n==0:
        fd(size)
    else:
        for angle in [0,60,-120,60]:
            left(angle)
            koch(size/3,n-1)
def main():
    setup(600,600)
    speed(0)
    penup()
    goto(-200,100)
    pendown()
    pensize(2)
    level=5
    koch(400,level)
    right(120)
    koch(400,level)
    right(120)
    koch(400,level)
    hideturtle
main()
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------