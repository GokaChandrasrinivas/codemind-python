n=input()
n=n.lower()
x=list(n.split(" "))
for i in x:
    print(min(i),max(i),end=" ")