
Money=input("请输入带有符号的钱数：")
if Money[-1]in['d','D']:
   M=6*eval(Money[:-1])
   print("转化后的钱数是{:.2f}Y".format(M))
elif Money[-1]in ['y','Y']:
   M=(eval(Money[:-1]))/6
   print("转换后的钱数是{:.2f}D".format(M))
else:
   print("输入格式错误")
