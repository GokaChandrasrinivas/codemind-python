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
    elif(i not in m):
        c=c+1
for i in m:
    if(i==" "):
        continue
    elif(i not in n):
        c=c+1
print(c)