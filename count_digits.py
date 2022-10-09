n=int(input())
l=list(map(int,input().split()))
for i in l:
    c=0
    if(i<0):
        i=-1*i
    elif(i==0):
        i=1
    while(i>0):
        r=i%10
        c=c+1
        i=i//10
    print(c,end=" ")