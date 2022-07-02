n=int(input())
es=0
a=list(map(int,input().split()))
for i in range(0,n):
    if(i%2==0):
        es=es+a[i]
print(es)
