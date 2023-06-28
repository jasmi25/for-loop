#19 Write a program to add first n terms of the following series using a while loop
#1/1! + 1/2! + 1/3! + …….. + 1/n!
a=1
n=int(input("enter nmber:-"))
for i in range(1,n+1):
    print(a,"/",i,"!","+",end="")
