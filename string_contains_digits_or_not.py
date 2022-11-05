n=int(input())
for i in range(n):
    s=input()#ajay
    for j in s:
        if(j.isdigit()):
            print("Yes")
            break
    else:
        print("No")