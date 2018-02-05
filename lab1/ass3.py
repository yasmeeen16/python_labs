


def num(n):
    outer_list=[]
    for x in range(n):
        innerlist=[]
        x=x+1;
        for z in range(x):
            z=z+1;
            innerlist.append(x*z)
        outer_list.append(innerlist)
    return outer_list

number=int(input("enter num : "));
print(num(number))


#------------------------------------



