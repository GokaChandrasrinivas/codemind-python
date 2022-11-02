n=input()
c=0
for i in n:
    if(i==" "):
        continue
    elif(i.isalpha()):
        continue
    else:
        c=c+1
print(c)