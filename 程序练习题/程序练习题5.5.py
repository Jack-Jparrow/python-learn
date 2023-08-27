def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
try:
    x=eval(input())
    if type(x)==type(1):
        if isprime(x):
            print(x,"是质数")

        else:
            print(x,"不是质数")
    else:
        print("请输入整数")
except:
    print("Error")
