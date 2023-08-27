from random import*
ls=("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz")
def mima():
    num=""
    for i in range(8):
        n=randint(0,61)
        num=num+ls[n]
    return num
for k in range(10):
    print("{}->{}".format(k,mima()))
