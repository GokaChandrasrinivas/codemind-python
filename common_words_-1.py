n=input()
m=input()
n=n.lower()
m=m.lower()
x=list(n.split(" "))
x1=list(m.split(" "))
c=0
c1=0
for i in x:
    if(i in x1):
        c=c+1
for i in x1:
    if(i in x):
        c1=c1+1
if(c>=c1):
    print(c)
else:
    print(c1)