l = list(input().split())
n,m = l[0],l[1]
l=[]
l=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
h=0
for i in l:
    if i in A:
        h+=1
    elif i in B:
        h-=1
    else:
        pass
print(h)
