from random import*
def randbirth():
    mon=randint(1,12)
    if mon in[1,3,5,7,8,10,12]:
        day=randint(1,31)
    elif mon==2:
        day=randint(1,28)
    else:
        day=randint(1,30)
    return mon*100+day
def main():
    ls=[]
    for i in range(23):
        ls.append(randbirth())
    if len(ls)==len(set(ls)):
        return 1
    else:
        return 0
try:
    poss=0
    n=eval(input())
    for i in range(n):
        if main()==1:
            poss=poss+1
    if(poss/n)>=0.5:
        print("相同生日的概率:{}".format(poss*100/n))
    else:
        print("相同生日的概率:{}".format(poss*100/n))
except:
    print("输入错误")
