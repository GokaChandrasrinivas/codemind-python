n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    while(i>0):
        r=i%10
        s=s+r
        i=i//10
print(s)