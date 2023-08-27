import time
scale=50
print("执行开始".center(scale//2,'-'))
t=time.clock()
for i in range(scale+1):
    a,b,c='*'*i,'.'*(scale-i),(i/scale)*100
    t -=time.clock()
    print("\n{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),end='')
    time.sleep(0.05)
print("\n"+"执行结束".center(scale//2,'-'))
