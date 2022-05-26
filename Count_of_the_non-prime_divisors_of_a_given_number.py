n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                c+=1
                break
        if i==1:
            c+=1
print(c)