import jieba
excludes={"什么","一个","我们","那里","你们","如今",
          "说道","知道","起来","姑娘","这里","出来",
          "他们","众人","自己","老太太","一面","太太",
          "只见","怎么","奶奶","两个","没有","不是",
          "不知","这个","听见","这样","进来","咱们",
          "告诉","就是","东西","回来","只是","大家",
          "老爷","只得","丫头","这些","不敢","出去",
          "所以","不过","的话","不好","姐姐","探春",
          "一时","不能","过来","心里","二爷","如此",
          "今日","银子","几个","答应","二人","还有",
          "只管","这么","说话","一回","那边","这话",
          "外头","打发","自然","今儿","罢了","屋里",
          "那些","听说","小丫头","如何","问道","看见"}
txt=open("红楼梦.txt","r",encoding='ANSI').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len (word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
