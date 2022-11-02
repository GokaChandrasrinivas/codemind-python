n=input()
c=0
n=n.lower()
temp=""
for i in range(len(n)-1,-1,-1):
    temp+=n[i]
if(temp==n):
    print(True)
else:
    print(False)