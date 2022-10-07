n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if(i in l1):
        continue
    else:
        l1.append(i)
c=0
for i in l1:
    if(l.count(i)==i):
        l2.append(i)
        c=c+1
if(c==0):
    print("-1")
else:
    for i in l2:
        print(i,end=" ")