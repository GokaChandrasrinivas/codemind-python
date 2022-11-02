n=input()
n=n.lower()
x=list(n.split(" "))
c=0
for i in x:
    temp=""
    
    for j in range(len(i)-1,-1,-1):
        temp+=i[j]
    if(temp==i):
        c=c+1
print(c)