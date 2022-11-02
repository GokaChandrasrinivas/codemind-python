n=input()
n=n.lower()
x=list(n.split(" "))
l=[]
for i in x[0]:
    c=0
    for j in range(1,len(x)):
        if(i in x[j]):
            c=c+1
    if(c==len(x)-1):
        l.append(i)
if(len(l)==0):
    print(-1)
else:
    for i in l:
        print(i,end="")

    