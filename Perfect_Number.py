n=int(input())#28
sum=0
for i in range(1,n):#28 4
    if(n%i==0):
        sum=sum+i#1+2+4+7+14
if(sum==n):
    print("True")
else:
    print("False")