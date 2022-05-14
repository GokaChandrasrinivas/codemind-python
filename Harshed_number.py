n=int(input())
sum=0
c=0
temp=n
while n:
    d=n%10
    n=n//10
    sum+=d
    c+=1
n=temp
if c==1:
    print('True')
elif n%sum==0:
    print('True')
else:
    print('False')