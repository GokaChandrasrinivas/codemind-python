n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[]
for i in l:
    if(i in l1):
        continue
    else:
        l1.append(i)
c=0
for i in l1:
    if(l.count(i)==k):
        c=c+1
        print(i,end=" ")
if(c==0):
    print("-1")