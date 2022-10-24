from collections import Counter

k = int(input())
l = list(map(int,input().split()))
c = Counter(l)

for i in c.keys():
    if c[i]==1:
        print(i)
