def minion_game(string):
    stuart=0
    kevin=0
    v=['A','E','I','O','U']
    
    for i in range(len(string)):
        if string[i] in v:
            kevin=kevin+(len(string)-i)
        else:
            stuart=stuart+(len(string)-i)
            
    if stuart>kevin:
        print("Stuart",stuart)
    elif kevin>stuart:
        print("Kevin",kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
