n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)-1,2):
    for j in range(0,l[i+1]):
        l1.append(l[i])
for i in l1:
    print(i,end=" ")