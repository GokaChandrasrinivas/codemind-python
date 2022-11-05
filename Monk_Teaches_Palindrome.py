t=int(input())
for i in range(t):
    n=input()
    s=""
    for j in range(len(n)-1,-1,-1):
        s=s+n[j]
    if(n==s):
        if(len(n)%2==0):
            print("YES",end=" ")
            print("EVEN")
        else:
            print("YES",end=" ")
            print("ODD")
    else:
        print("NO")
    