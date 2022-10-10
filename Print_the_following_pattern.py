n=int(input())
k=0
m=n-1
temp=n
for i in range(0,n):
    for j in range(0,n):
        if(j==k or j==m):
            print(temp,end=" ")
        else:
            print(" ",end="")
    k=k+1
    m=m-1
    temp=temp-1
    print()
