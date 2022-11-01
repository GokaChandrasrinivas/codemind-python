n=input()
x=list(n.split())
for i in x:
    if(x.index(i)%2==0):
        for j in range(len(i)-1,-1,-1):
            print(i[j],end="")
    else:
        print(end=" ")
        print(i,end=" ")
    