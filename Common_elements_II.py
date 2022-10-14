n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
l4=[]
l5=[]
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
    if(i in l2):
        continue
    else:
        l5.append(i)
for i in l4:
    if(i in l1 and i not in l5):
        continue
    else:
        l5.append(i)
for i in l5:
    print(i,end=" ")