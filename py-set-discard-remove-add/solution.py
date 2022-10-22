n=int(input())
s=set(map(int,input().split()))

for i in range(int(input())):
    inp = input().split()
    if inp[0]=='remove':
        if int(inp[1]) in s:
            s.remove(int(inp[1]))
        else:
            pass
    elif inp[0]=='discard':
        s.discard(int(inp[1]))
    elif inp[0]=='pop':
        if len(s)==0:
            pass
        else:
            s.discard(next(iter(s)))
            ### POP didn't work as expected lmao
print(sum(s))
