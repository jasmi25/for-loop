#    1
#   22
#  333
# 4444
#55555
a=int(input("enter number"))
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(" ",end="")
    for n in range(1,i+1):
        print(i,end="")
    print()
    
