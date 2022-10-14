n=int(input())
l=list(map(int,input().split()))
if(l.index(min(l))>l.index(max(l))):
    r1=l.index(max(l))
    r2=l.index(min(l))
else:
    r1=l.index(min(l))
    r2=l.index(max(l))
c=0
for i in range(r1,r2+1):
    if(l[i]==1):
        continue
    for j in range(2,int(l[i]**0.5)+1):
        if(l[i]%j==0):
            break
    else:
            c=c+1
print(c)