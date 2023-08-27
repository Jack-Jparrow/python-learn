dayup,dayfactor=1.0,0.01
for i in range(365):
    if i % 16 in [1,2,3]:
        dayup=dayup*1
    else:
        if i % 16 in [4,5,6,7,8,9,10,11,12,13,14,15]:
            dayup=dayup*(1+dayfactor)
print("15休1的力量:{:.2f}.".format(dayup))
