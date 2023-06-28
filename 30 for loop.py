#30. Write a program to find the sum of following series
#1 + 8 + 27 …………n terms
a=int(input("enter number"))
sum=0
b=1
for i in range(1,a+1):
    b=i**3
    sum=sum+b
print(sum)
    
