#37.Write a program to print the factorial of a number
a=int(input("enter number"))
factorial=1
for i in range(a,0,-1):
    factorial*=i
print(factorial)
    
