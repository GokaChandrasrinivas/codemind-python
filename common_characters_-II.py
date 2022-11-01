n=input()
m=input()
n=n.lower()
m=m.lower()
n=set(n)
m=set(m)
n=list(n)
m=list(m)
c=0
for i in n:
    if(i==" "):
        continue
    elif(i in m):
        c=c+1
print(c)