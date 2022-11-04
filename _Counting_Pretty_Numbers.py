t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    c=0
    for j in range(n,m+1):
        while(j>0):
            r=j%10
            if(r==2 or r==3 or r==9):
                c=c+1
                break
            else:
                break
    print(c)
        