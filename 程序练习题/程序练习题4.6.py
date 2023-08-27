from random import*
time=eval(input())
first=0
change=0
for i in range(time):
    car=randint(0,2)
    you=randint(0,2)
    if you ==car:
        first=first+1
    else:
        change=change+1
first_per=first/time
change_per=change/time
print("第一次猜中：{:.2f}% ,第二次猜中：{:.2f}%".format(first_per*100,change_per*100))
