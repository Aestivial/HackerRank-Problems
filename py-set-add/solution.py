n = int(input())
s=set()
u=0
for i in range(n):
    p=input()
    if p in s:
        pass
    else:
        u+=1
    s.add(p)
print(u)
