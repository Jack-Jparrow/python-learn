import os
 
for i in range(136, 251):#左闭右开
    res = "QZJT_JAVA_" + str(i) + ".java"
    # print(type(res))
    open("%s" % res, "w+")
