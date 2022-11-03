n=input()
u=[]
l=[]
for i in n:
    if(i==" "):
        continue
    if(i.isupper()):
        u.append(i)
    elif(i.islower()):
        l.append(i)
if(len(u)==0):
    print(min(l))
elif(len(l)==0):
    print(min(u))
elif(min(u).lower()==min(l)):
    print(min(l))
elif(min(u).lower()!=min(l)):
    if(min(u).lower()>min(l)):
        print(min(l))
    else:
        print(min(u))
else:
    print(min(u))