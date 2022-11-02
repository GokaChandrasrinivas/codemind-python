s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
c=0
s1=set(s1)
s1=list(s1)
s2=set(s2)
s2=list(s2)
if(len(s1)>=len(s2)):
    for i in s1:
        if(i in s2):
            c=c+1
else:
    for i in s2:
        if(i in s1):
            c=c+1
if(c==len(s1)):
    print(True)
else:
    print(False)