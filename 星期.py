weekstr="星期一星期二星期三星期四星期五星期六星期日"
n=eval(input("请输入星期几数字："))
if 1<=n<=7:
    k=3*(n-1)
    print(weekstr[k:k+3])

else:
    print("error")
