n=input()
v=0
c=0
d=0
w=0
for i in n:
    if(i in "aeiouAEIOU"):
        v=v+1
    elif(i.isalpha() and i not in "AEIOUaeiou"):
        c=c+1
    elif(i.isdigit()):
        d=d+1
    elif(i==" "):
        w=w+1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)