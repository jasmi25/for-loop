#22 Write a program to accept 10 numbers from the user and display it’s average
sum=0
for i in range(1,11):
    a=int(input("enter number"))
    sum=sum+a
print(sum)
average=sum//10
print(average)
