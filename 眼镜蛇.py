from turtle import*
setup(650,350,200,200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("red")
seth(-40)
for i in range(2):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(80,540)
fd(280*2/3)
circle(80,360)


