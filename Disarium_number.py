n=int(input())
temp=n
temp1=n
c=0
 
while(n>0):
    r=n%10
    c=c+1
    n=n//10
m=c
r=0
s=0
for i in range(m,0,-1):
    r=temp%10
    s=s+r**i
    temp=temp//10
if(s==temp1):
    print(True)
else:
    print(False)
     