#21. Write a python program to sum the sequence
#1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!
a=1
n=int(input("enter number"))
for i in range(1,n):
    print(a,"+",a,"/",i,"!","+",end="")
