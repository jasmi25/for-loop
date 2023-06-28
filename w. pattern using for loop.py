#A 
#A B 
#A B C 
#A B C D 
#A B C D E 
a=int(input("enter number"))
for i in range(65,a+1):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()
