#26. Write a program to print the following series till n terms.
#2 , 22 , 222 , 2222 _ _ _ _ _ n terms
a=int(input("enter number"))
b=2
for i in range(1,a+1):
    print(str(b)*i,end=",")
