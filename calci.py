a=int(input("enter the value"))
b=int(input("enter the value"))
print("which method did you want")
print("1-addition")
print("2-subtraction")
print("3-multiplication")
print("4-division")
method=int(input("enter the method number"))
if(method==1):
    add=a+b
    print("addition",add)
elif(method==2):
    sub=b-a
    print("subtraction",sub)
elif(method==3):
    mul=a*b
    print("multiplication",mul)
elif(method==4):
    div=b//a
    print("division",div)
else:
    print("the default method")

        
