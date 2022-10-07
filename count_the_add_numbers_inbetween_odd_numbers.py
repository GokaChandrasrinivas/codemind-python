n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n,2):
    if(l[i]%2==1):
        c=c+1
print(c)