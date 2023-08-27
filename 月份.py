monthstr="JanFebMarAprMayJunJulAugSepOctNovDec"
n=eval(input("请输入月份数字："))
if 1<=n<=12:
    k=3*(n-1)
    print(monthstr[k:k+3])
else:
    print("error")
