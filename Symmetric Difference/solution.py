# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
M = input().split()
M = set(map(int,M))

n = int(input())
N = input().split()
N = set(map(int,N))

m = M.difference(N)
m.update(N.difference(M))

for i in sorted(m):
    print(i)