n=int(input())
l=list(map(int,input().split()))
if(n%2==1):
    l.append(0)
    for i in l:
        print(i,end=" ")
else:
    for i in range(0,n):
        print(l[i],end=" ")
    