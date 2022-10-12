n=int(input())
temp=n
c=0
while(n>0):
    r=n%10
    c=c+1
    n=n//10
if(c==10 and r!=0):
    print("Valid")
else:
    print("Invalid")
