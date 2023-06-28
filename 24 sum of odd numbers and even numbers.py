#24 Write a program to display sum of odd numbers and even numbers separately that fall between two
#numbers accepted from the user.(including both numbers) 100 and 500
e_s=0
o_s=0
a=int(input("enter number"))
for i in range(1,a+1):
    if i%2==0:
        e_s+=i
    else:
        o_s+=i
print(e_s)
print(o_s)
