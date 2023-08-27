import keyword
f=open("lxt62.py")
content=f.read()
f.close()
table=['range','print','list','set','keyword','kwlist','end']
fs=''
temp=""
for ch in content:
    if ch.isalpha():
        temp=temp+ch
    else:
        if(not keyword.iskeyword(temp) and temp in table):
            temp=temp.upper()
        fs=fs+temp
        fs=fs+ch
        temp=''
f=open("daxie.py","w")
f.write(fs)
f.close()
