#36. Accept two numbers from the user and display sum of even numbers between them(including both)
sum=0
a=int(input("enter number"))
for i in range(1,a+1):
    if i%2==0:
        sum=sum+i
print(sum)
