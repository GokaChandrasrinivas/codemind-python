m,n=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
l4=[]
c=0
for i in l1:
    if(i in l3):
        continue
    else:
        l3.append(i)
for i in l2:
    if(i in l4):
        continue
    else:
        l4.append(i)
for i in l3:
    if(i in l4):
        c=c+1
print(c)