n=int(input())
l=list(map(int,input().split()))
s=0
for i in set(l):
    s=s+i
print(s)