#31. Write a program to find the sum of following series:
#1 + 2 + 6 + 24 + 120 . . . . . n terms
b=1
a=int(input("enter number"))
sum=0
for i in range(1,a+1):
    b=b*i
    sum+=b
print(sum)
