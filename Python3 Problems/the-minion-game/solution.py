def minion_game(string):
    stuart=0
    kevin=0
    v=['A','E','I','O','U']
    p=[string[i:j] for i in range(len(string)) 
                    for j in range(i+1, len(string)+1)]
    for i in p:
        if i[0] in v:
            kevin+=1
            
        else:
            stuart+=1
    if stuart>kevin:
        print("Stuart",stuart)
    elif kevin>stuart:
        print("Kevin",kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
