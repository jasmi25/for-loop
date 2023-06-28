#9. Write a program to display all even numbers that fall between two numbers (exclusive both numbers)
#entered by the user
a=int(input("enter number"))
b=int(input("enter number"))
for a in range(a,b):
    if a%2==0:
        print(a)

