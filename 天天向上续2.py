dayup,dayfactor=1.0,0.01
for i in range(365):
    if i % 11 in [1,2,3]:
        dayup=dayup*1
    else:
        if i % 11 in [4,5,6,7,8,9,10]:
            dayup=dayup*(1+dayfactor)
print("10休1的力量:{:.2f}.".format(dayup))

