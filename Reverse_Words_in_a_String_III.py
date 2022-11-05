n=input()
x=list(n.split(" "))
for i in x:#ajay
    s=""
    for j in range(len(i)-1,-1,-1):
        s=s+i[j]
    print(s,end=" ")