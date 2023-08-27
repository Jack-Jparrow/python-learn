from turtle import*
from datetime import*
speed(10)
def drawGap():
    penup()
    fd(5)
def drawLine(draw):
    pendown() if draw else penup()
    fd(40)
    right(90)
def drawDigit(d):
    pencolor("red")
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    pencolor("green")
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    pencolor("yellow")
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    pencolor("brown")
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    left(90)
    pencolor("blue")
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    pencolor("violet")
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    pencolor("orange")
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    left(180)
    penup()
    fd(20)
def drawDate(date):
    pencolor("black")
    for i in date:
        if i == '-':
            write('年',font=("Arial",18,"normal"))
            pencolor("light blue")
            fd(40)
        elif i == '=':
            write('月',font=("Arial",18,"normal"))
            pencolor("light green")
            fd(40)
        elif i == '+':
            write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
def main():
    setup(800,350,200,200)
    penup()
    fd(-300)
    pensize(5)
    drawDate(datetime.now().strftime('%Y-%m=%d+'))
    hideturtle()
main()
