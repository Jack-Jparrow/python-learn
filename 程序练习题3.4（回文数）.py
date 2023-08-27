n=input("请输入一个5位数字：")
k=len(n)
if k==5:
    s=n[4]+n[3]+n[2]+n[1]+n[0]
    if n==s:
        print("回文")
    else:
        print("非回文")
else:
    print("error")
