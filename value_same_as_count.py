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
        c=c+1
print(c)
    
        