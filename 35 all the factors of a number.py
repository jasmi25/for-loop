#35 Write a program to print all the factors of a number using a while loop
a=int(input("enter number"))
for i in range(1,a+1):
    if a%i==0:
        print(i)
