n=input()
c=0
l=[]
for i in n:
    if(i in "aeiou"):
        c=c+1
        l.append(i)
    elif(i in "AEIOU"):
        c=c+1
        l.append(i)
l1=[]
for i in l:
    if(i in l1):
        continue
    else:
        l1.append(i)
if(c==0):
    print(-1)
else:
    print(*l1)