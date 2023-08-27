sieve=[True]*101
for i in range(2,10):  #“10”是改变最大数范围的
    if sieve[i]:
        print(i,end=" ")
        for j in range(i*i,100,i):
            sieve[j]=False
