def func(x):
    return x,x**3
a,b='dog','tihger'
a,b=(b,a)
import math
for x,y in ((1,0),(2,5),(3,6)):
    print(math.hypot)
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
from math import sqrt
def getNum():
    nums=[]
    iNumStr=input("请输入数字(直接输入回车退出)：")
    while iNumStr!="":
        nums.append(eval(iNumStr))
        iNumStr=input("请输入数字(直接输入回车退出)：")
    return nums
def mean(numbers):
    s=0.0
    for num in numbers:
        s=s+num
    return s/len(numbers)
def dev(numbers,mean):
    sdev=0.0
    for num in numbers:
        sdev=sdev+(num-mean)**2
    return sqrt(sdev/(len(numbers)-1))
def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med
n=getNum()
m=mean(n)
print("平均值:{},方差:{:.2},中位数:{}.".format(m,dev(n,m),median(n)))
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
import jieba
jieba.lcut("中国是一个伟大的国家")
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
def getText():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt=txt.replace(ch," ")
    return txt
hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
excludes={"the","and","of","you","a","i","my","in"}
def getText():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt=txt.replace(ch," ")
    return txt
hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
import jieba
txt=open("三国演义.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
#----------------------------------------------------------
print("                   ")
#----------------------------------------------------------
import jieba
excludes={"将军","却说","荆州","二人","不可","不能","如此"}
txt=open("三国演义.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="诸葛亮" or word=="孔明曰":
        rword="孔明"
    elif word=="关公" or word=="云长":
        rword="关羽"
    elif word=="玄德" or word=="玄德曰":
        rword="孔明"
    elif word=="孟德" or word=="丞相":
        rword="曹操"
    else:
        rword=word
    counts[word]=counts.get(rword,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(5):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
