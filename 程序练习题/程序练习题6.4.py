txt=input("请输入英文句子：")
counts={}
ex={',','!',';',':','?','.'}
txt=txt.lower()
for i in txt:
    if i=='' or i in ex:
        continue
    else:
        counts[i]=counts.get(i,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for u in range(len(items)):
    alpha,count=items[u]
    print("{}->{}".format(alpha,count))
