#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * *
a=int(input("enter number"))
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(" ",end="")
    for c in range(1,i+1):
        print("*",end=" ")
    print()
