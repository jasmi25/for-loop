a=int(input("enter number"))
b=1
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(" ",end=" ")
    for k in range(1,b+1):
        print("*",end=" ")
    b=b+2
    print()
