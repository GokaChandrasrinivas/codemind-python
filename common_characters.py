n=input()
m=input()
n=n.lower()
m=m.lower()
s=""
for i in n:
    if(i==" "):
        continue
    elif(i in m):
        s=s+i
s=set(s)
if(len(s)==0):
    print(-1)
else:
    for i in sorted(s):
        print(i,end="")