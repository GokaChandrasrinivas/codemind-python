n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if(i in l1):
        continue
    else:
        l1.append(i)
for i in l1:
    print(i,l.count(i),end=" ")