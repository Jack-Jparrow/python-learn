from turtle import*
from datetime import*
speed(10)
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
    for i in date:
        drawDigit(eval(i))
def main():
    setup(800,350,200,200)
    penup()
    fd(-300)
    pensize(5)
    drawDate(datetime.now().strftime('%Y%m%d'))
    hideturtle()
main()
