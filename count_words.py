n=input()
x=list(n.split(" "))
c=0
for i in x:
    if((i[0] in "AEIOUaeiou") and (i[-1] not in "AEIOUaeiou")):
        c=c+1
print(c)