n=input()
c=0
for i in "aeiou":
    if(i in n):
        c=c+1
if(c==5):
    print(True)
else:
    print(False)