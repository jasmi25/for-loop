#18 Write a program to convert binary to decimal
a=str(input('entre the binary number')) 
b=list(a) 
j=int(len(a)-1) 
print(j) 
a=0 
for i in b: 
    if i=='1': 
        a=a+(2**j) 
    j=j-1 
print(a) 
