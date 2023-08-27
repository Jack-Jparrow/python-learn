from random import*
x=randint(0,9)
n=0
while True:
    y=eval(input(""))
    if y==x:
        print("预测",n,"次，你猜中了")
        break
    elif y>x:
        print("遗憾，太大了")
    else:
        print("遗憾，太小了")
