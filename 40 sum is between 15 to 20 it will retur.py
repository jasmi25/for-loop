#40.Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
a=int(input("enter number"))
b=int(input("enter number"))
c=a+b
for i in range(1,3):
    if c>=15 and c<=20:
        print("return 20")
    else:
        print("not return 20")
