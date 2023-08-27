def multi(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return(s)
x=eval(input())
print(multi(x))
