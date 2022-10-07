n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    if(l[i]%2==1):
        print(False)
        break
else:
    print(True)