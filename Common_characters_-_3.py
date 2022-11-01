n=input()
x=list(n.split(" "))
n=n.lower()
n=set(n)
n=list(n)
l=[]
for i in n:
    c=0
    for j in x:
        if(i in j):
            c=c+1
            continue
    if(c==len(x)):
        l.append(i)
if(len(l)==0):
    print(-1)
else:
    print(min(l))