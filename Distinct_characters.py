n=input()
n=n.lower()
s=set(n)
s=sorted(s)
s=list(s)
for i in s:
    if(i==" "):
        continue
    else:
        print(i,end="")