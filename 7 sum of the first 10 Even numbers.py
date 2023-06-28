#7 Write a program to print the sum of the first 10 Even numbers
sum=0
for i in range(1,11):
    if i%2==0:
        sum=sum+i
print(sum)
