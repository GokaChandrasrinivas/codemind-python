n=int(input())
c=0
temp=n
while n!=0:
    d=n%10
    n=n//10
    c+=1
n=temp
b=n*n
if b%(10**c)==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')