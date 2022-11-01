n=input()
x=list(n.split(" "))
for i in range(len(x)-1,-1,-1):
    for j in range(len(x[i])-1,-1,-1):
        print(x[i][j],end="")
    print(end=" ")