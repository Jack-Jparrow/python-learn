def getnum():
    ls=[]
    n=input("请输入一个整数:")
    while n!="":
        ls.append(n)
        n=input("请输入一个整数:")
    return ls
def judge(num):
    k=len(num)
    for i in range(k):
        if num[i] in num[i+1:k]:
            return True
    else:
        return False
mm=getnum()
print(judge(mm))
