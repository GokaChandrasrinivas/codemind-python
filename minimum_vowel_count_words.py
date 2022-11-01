n=input()
n=n.lower()
x=list(n.split(" "))
l=[]
for i in x:
    c=0
    for j in i:
        if(j in "aeiou"):
            c=c+1
    l.append(c)
print(l.count(min(l)))