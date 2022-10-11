n=int(input())
l=[]
for i in range(0,(n//2)+1):
    for j in range(i,(n//2)+1):
        if(i*j==n):
            l.append(i)
            l.append(j)
l1=[]
for i in l:
    for j in range(2,(i//2)+1):
        if(i%j==0):
            break
    else:
        l1.append(i)
c=0
for i in range(0,len(l1)):
    if(n==0):
        print(0)
        break
    for j in range(i,(len(l1))):
        if(l1[i]*l1[j]==n):
            c=c+1
            print(l1[i],l1[j])
if(c==0):
    print(-1)
