n=int(input())
temp=n#1124
sum=0
pro=1
r=0
while(n!=0):
    r=n%10#4 2 1 1
    sum=sum+r#4+2+1+1
    n=n//10#
while(temp!=0):#1124
    r=temp%10#4 2
    pro=pro*r
    temp=temp//10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")