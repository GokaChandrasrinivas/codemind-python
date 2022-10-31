n=input()
n=n.lower()
s=[]
for i in n:
    if(i==" "):
        continue
    s.append(i)
s=set(s)
s=list(s)
l=[]

for i in s:
    if(n.count(i)==1):
        l.append(i)
for i in sorted(l):
    print(i,end="")
