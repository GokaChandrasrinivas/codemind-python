from itertools import permutations
a,b=map(int,input().split())
s=[str(i) for i in range(1,a+1)]
s=''.join(s)
lst=list(permutations(s))
res=lst[b-1]
res=''.join(res)
print(res)