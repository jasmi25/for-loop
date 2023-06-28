#15. Write a program to print the Fibonacci series till n terms (Accept n from user)
a=int(input("enter number"))
n1=0
n2=1
s=0
print(n1,n2,end=" ")
for i in range(0,a+1):
    s=n1+n2
    n1=n2
    n2=s
    print(s,end=" ")
