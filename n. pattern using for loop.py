#0 
#0 1 
#0 2 4 
#0 3 6 9 
#0 4 8 12 16
a=int(input("enter number"))
for i in range(0,a):
    for j in range(0,i+1):
        print(j*i,end=" ")
    print()
