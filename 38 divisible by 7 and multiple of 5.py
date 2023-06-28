#38.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and
#2700 (both included)
a=int(input("enter number"))
for i in range(1500,a+1):
    if i%5==0 or i%7==0:
        print(i,"divisible by 7 and multiple of 5")
    else:
        print(i,"not divisible by 7 and multiple of 5")
