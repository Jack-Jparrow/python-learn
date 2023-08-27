def main():
    ls=[]
    n=input("请输入一个整数:")
    while n!="":
        ls.append(n)
        n=input("请输入一个整数:")
    else:
        print("正在处理，请稍等")
        judge(ls)
def judge(n):
    if len(n)==len(set(n)):
        print("鉴定完毕，没有重复的元素")
    else:
        print("有重复的元素，总共有{}个".format(len(n)-len(set(n))))
main()
