n=int(input())
a=list(map(int,input().split()))
es=0
for i in a:
    if(i%2==0):
        es=es+i
print(es)