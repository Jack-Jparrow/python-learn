from math import*
for x in range(100, 200):
    for y in range(2, round(sqrt(x))+1):
        if x % y == 0:
            break
    else:
        print(x, end=',')
