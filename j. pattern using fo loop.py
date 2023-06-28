#    1
#   21
#  321
# 4321
#54321
a=int(input("enter number"))
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(" ",end="")
    for c in range(i,0,-1):
        print(c,end="")
    print()
