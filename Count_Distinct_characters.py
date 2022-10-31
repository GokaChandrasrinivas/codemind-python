n=input()
n=n.lower()
s=[]
for i in n:
    if(i==" "):
        continue
    s.append(i)
s=set(s)
s=list(s)
print(len(s))