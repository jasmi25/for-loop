#34 Write a program to print only odd numbers from the given list using a while loop . L = [23, 45, 32, 25, 46,
#33, 71, 90]
list=[23, 45, 32, 25, 46,33, 71, 90]
for i in range(1,len(list)):
    b=list[i]
    if b%2==0:
        print(b,end=" ")
