n = int(input())
A = set(map(int,input().split()))
N = int(input())
for i in range(N):
    r=input().split()
    if r[0] == 'update':
        A.update(set(map(int,input().split())))
    elif r[0] == 'intersection_update':
        A.intersection_update(set(map(int,input().split())))
    elif r[0] == 'difference_update':
        A.difference_update(set(map(int,input().split())))
    elif r[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(set(map(int,input().split())))
    else:
        pass
print(sum(A))
