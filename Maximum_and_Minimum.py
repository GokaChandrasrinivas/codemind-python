n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if(i in l1):
        continue
    else:
        l1.append(i)
for i in l1:
    if(l.count(i)==i):
        l2.append(i)
if(len(l2)==0):
    print("-1")
else:
    print(min(l2),max(l2))
