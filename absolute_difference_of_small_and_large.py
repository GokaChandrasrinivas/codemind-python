n=input()
x=list(n.split(" "))
for i in x:
    print(abs(ord(min(i))-ord(max(i))),end=" ")