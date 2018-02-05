




def area(shape):
    if shape is "t":
        base=int(input("enter base : "))
        height=int(input("enter height : " ))
        area= 0.5*base*height;
        return area
    elif shape is "r":
        width=int(input("enter width : "))
        height=int(input("enter height : " ))
        area= width*height;
        return area
    elif shape is "s":
        height=int(input("enter height : "))
        area= height*height;
        return area
    elif shape is "c":
        radius=int(input("enter radius : "))
        area= 3.14*radius**2;
        return area
    else:
        return "shape not found"   



#shape= input("enter shape from t,r,s,c :  ")
print(area('t'))
print(area('c'))