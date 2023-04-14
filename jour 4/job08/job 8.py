# Liste d'entiers
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme = 0

for x in L:
    # Vérifier si la valeur est paire
    if x % 2 == 0:
        somme += x

# Afficher la somme des valeurs paires
print("La somme des valeurs paires dans la liste est :", somme)
