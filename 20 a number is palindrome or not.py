#20 Write a program to check whether a number is palindrome or not
a=input("enter number")
r=a
for i in range((len(a)-1),-1,-1):
    print(a[i],end="")
r=int(r)
if (r==i):
    print("number is palindrome ")
else:
    print("number is not palindrome ")
    


