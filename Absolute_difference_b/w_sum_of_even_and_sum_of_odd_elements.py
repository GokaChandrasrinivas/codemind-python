n=int(input())
es=0
os=0
a=list(map(int,input().split()))
for i in a:
    if(i%2==0):
        es=es+i
    else:
        os=os+i
print(abs(es-os))