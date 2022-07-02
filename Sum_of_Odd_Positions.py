n=int(input())
a=list(map(int,input().split()))
os=0
for i in range(0,n):
    if(i%2==1):
        os=os+a[i]
print(os)