n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=[]
l3=[]
l4=[]
for i in l:
    if(i in l2):
        continue
    else:
        l2.append(i)
for i in l1:
    if(i in l3):
        continue
    else:
        l3.append(i)
for i in l2:
    if(i in l3):
        continue
    else:
        l4.append(i)
for i in l3:
    if(i in l2 and i not in l4):
        continue
    else:
        l4.append(i)
print(len(l4))