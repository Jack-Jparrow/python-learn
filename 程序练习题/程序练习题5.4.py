def multi(n):
    s=1
    for i in n:
        s=s*i
    return s
try:
    x=list(eval(input("请输入多个数，中间用逗号分隔")))
    print(multi(x))
except:
    print("Error")
