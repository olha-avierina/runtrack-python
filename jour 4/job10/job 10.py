# Liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser le produit à 1
produit = 1
for valeur in L:
    # Vérifier si la valeur est dans l'intervalle [25, 90]
    if 25 <= valeur <= 90:
        # Multiplier la valeur au produit
        produit *= valeur
print("Le produit des valeurs dans l'intervalle [25, 90] est :", produit)
