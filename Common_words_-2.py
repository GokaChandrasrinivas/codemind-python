n=input()
m=input()
x=list(n.split(" "))
y=list(m.split(" "))
c=0
for i in x:
    if(i in y and x.count(i)==1 and y.count(i)==1):
        c=c+1
print(c)