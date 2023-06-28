#11. Write a program to find the sum of the digits of a number accepted from the user
a=input("enter number")
sum=0
for i in range(0,len(a)):
    sum=sum+int(a[i])
print(sum)
