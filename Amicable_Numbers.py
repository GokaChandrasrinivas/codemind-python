n=int(input())
m=int(input())
sum1=0
sum2=0
for i in range(1,n):
    if(n%i==0):
        sum1+=i
for i in range(1,m):
    if(m%i==0):
        sum2+=i
if(sum1==m and sum2==n):
    print("Amicable")
else:
    print("Not Amicable")