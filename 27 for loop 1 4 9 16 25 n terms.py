#27 Write a program to print the following series till n terms.1 4 9 16 25 _ _ _ _ _ n terms
a=int(input("enter number"))
for i in range(1,a+1):
    b=i*i
    print(b,end=" ")
