num=input("enter rows number : ")
rang=range(int(num))
for i in rang:
    print(" "*(int(num)-1-i)+"*"*(i+1))