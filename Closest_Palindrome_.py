n=int(input())
temp=n
temp1=n
temp2=n
while(True):
    s=0
    r=0
    temp=temp+1
    n=temp
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    if(s==temp):
        break
while(True):
    s1=0
    r=0
    temp1=temp1-1
    n=temp1
    while(n>0):
        r=n%10
        s1=s1*10+r
        n=n//10
    if(s1==temp1):
        break
if((temp2-s1)>(s-temp2)):
    print(s)
elif((temp2-s1)==(s-temp2)):
    print(s1,end=" ")
    print(s,end=" ")
else:
    print(s1)
       