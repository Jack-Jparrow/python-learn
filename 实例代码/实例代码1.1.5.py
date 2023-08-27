from datetime import datetime
now=datetime.now()
print(now)
a=now.strftime("%x")
b=now.strftime("%X")
print("{}\n{}".format(a,b))
