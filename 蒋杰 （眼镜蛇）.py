from turtle import *
def snake1(radius,angle,length):
    seth(-40)
    for i in range(length):
        circle(radius,angle)
        circle(-radius,angle)
def snake2(radius,angle):       
    circle(radius,angle/2)
    fd(radius)
    circle(60,540)
    fd(200*2/3)
    pencolor("brown")
    circle(60,360)
    fd(120)
def main():
    setup(650,350,200,200)
    penup()
    fd(-250)
    pendown()
    pensize(20)
    seth(-40)
    pencolor("orange")
    snake1(40,80,1)
    pencolor("purple")
    snake1(40,80,1)
    pencolor("yellow")
    snake1(40,80,1)
    pencolor("blue")
    snake1(40,80,1)
    pencolor("green")
    snake2(40,80)
main()

plt.text(hhh)