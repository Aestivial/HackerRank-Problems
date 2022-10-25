def merge_the_tools(string, k):
    chunks=[]
    i=0
    while i<len(string):
        if i+k<len(string):
            chunks.append(string[i:i+k])
        else:
            chunks.append(string[i:len(string)])
        i+=k
        
    for x in chunks:
        s=""
        for i in x:
            if i not in s:
                s=s+i
            else:
                pass
        print(s)    

if __name__ == '__main__':
