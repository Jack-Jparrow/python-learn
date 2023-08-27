def isnum(n):
    if type(n)==type(1) or type(n)==type(1.2) or type(n)==type(4j):
        return True
    else:
        return False
try:
    x=eval(input())
    if isnum(x):
        print("True")
    else:
        print("False")
except:
    print("Error")
    
