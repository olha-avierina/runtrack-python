

def fonction (a,b,c):
    if a==b and b==c and c==a:
        return("c'est un triangle equilateral")
    elif a==b or b==c or c==a:
        return ("c'est un rectangle triangle")
    elif c==(a**2+b**2)**0.5:
        return("c'est un rectangle, isocèle triangle")
    # Si nomders negatif
    elif a<=0 or b<=0 or c<=0:
        return("entre des valeurs superieures")
    else:
        return("c'est un triangle")
    
print (fonction(5,5,5))