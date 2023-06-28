#12 Write a program to find the product of the digits of a number accepted from the user
a=input("enter number")
product=1
for i in range(0,len(a)):
    product=product*int(a[i])
print(product)
