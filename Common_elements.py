n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=[]
for i in l:
    if(i in l2):
        continue
    else:
        l2.append(i)
for i in l2:
    if(i in l1):
        print(i,end=" ")