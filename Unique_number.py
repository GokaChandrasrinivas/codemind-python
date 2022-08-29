n=int(input())
m=str(n)
k=''
for i in m:
    if(i in k):
        print("Not Unique Number")
        break
    else:
        k+=i
if(len(k)==len(m)):
    print("Unique Number")