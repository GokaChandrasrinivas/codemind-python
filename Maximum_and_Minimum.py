n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if(i in l1):
        continue
    else:
        l1.append(i)
l2=[]
c=0
for i in l1:
    if(l.count(i)==i):
        c=c+1
        l2.append(i)
if(c==0):
    print(-1)
else:
    print(min(l2),max(l2))