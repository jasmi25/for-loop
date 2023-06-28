#17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is
#equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)
a=input("enter number")
arm=0
for i in range(0,len(a)):
    b=a[i]
    c=(int(b)**3)
    arm=c+arm
print(arm)
if int(a)==arm:
    print("armstrong number")
else:
    print("no armstrong number")

