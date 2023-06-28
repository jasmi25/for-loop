#10 Write a program to check whether a number is prime or not
n=int(input("enter number"))
for i in range(2,n):
    if n%i==0:
        print("not prime number")
        break
else:
    print("it is prime number")
