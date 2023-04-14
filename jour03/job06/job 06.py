#Function for piramid
symbol = "abcdefghijklmnopqrstuvwxyz"*10
Letter = 1
Line = 0

while Line < len(symbol):
    for j in range(Letter):
        if Line < len(symbol):
            print(symbol[Line], end='')
            Line +=1
        else:
            break
    print()
    Letter +=1




