n=int(input())
l=list(map(int,input().split()))
l.reverse()
num=0
for i in range(0,n):
    if(l[i]==0):
        continue
    else:
        num=num+2**i
print(num)