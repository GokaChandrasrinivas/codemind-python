n=input()
x=list(n.split(" "))
p=1
for i in x:
    if(i[0] in "aeiouAEIOU"):
        i=i+"ma"+("a"*p)
        print(i,end=" ")
    elif( i[0] not in "AEIOUaeiou"):
        s=""
        temp=i[0]
        for j in range(1,len(i)):
            s=s+i[j]
        s=s+temp+"ma"+("a"*p)
        print(s,end=" ")
    p=p+1