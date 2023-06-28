#1
#23
#456
#78910
a=int(input("enter number"))
b=1
for i in range(1,a+1,+b):
    for j in range(1,i+1,):
        print(b,end=" ")
        b=b+1
    print()
