#    1
#   12
#  123
# 1234
#12345
a=int(input("enter number"))
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(" ",end="")
    for k in range(1,i+1):
            print(k,end="")
    print()
