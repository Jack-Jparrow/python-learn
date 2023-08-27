def getnum():
    num=[]
    n=input()
    while n!="":
        num.append(n)
        n=input()
    return num
mmm=getnum()
def judge(num):
    k=len(num)
    for i in range (k):
        if num[i] in num[i+1:k]:
            return True
    else:
        return False
print(judge(mmm))
    
        
