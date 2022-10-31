n=input()
x=list(n.split(" "))
for i in x:
    for j in range(len(i)-1,-1,-1):
        print(i[j],end="")
    print(end=" ")