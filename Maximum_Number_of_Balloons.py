n=input()
l=[]
l.append(n.count("b"))
l.append(n.count("a"))
l.append(n.count("l")//2)
l.append(n.count("o")//2)
l.append(n.count("n"))
print(min(l))