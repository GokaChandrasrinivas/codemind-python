n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    c=0
    while(i>0):
        r=i%10
        c=c+1
        i=i//10
    k.append(c)
print(k.count(min(k)))
