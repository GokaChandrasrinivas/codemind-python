n=input()
x=list(n.split(" "))
l=[]
for i in x:
    l.append(len(i))
print(min(l))