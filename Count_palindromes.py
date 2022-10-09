n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    temp=i
    s=0
    while(i>0):
        r=i%10
        s=s*10+r
        i=i//10
    if(s==temp):
        c=c+1
print(c)