# Liste d'entiers
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser les variables pour le maximum et le minimum
max_val = L[0]  
min_val = L[0]  

for valeur in L: 
    if valeur > max_val:
        max_val = valeur

    if valeur < min_val:
        min_val = valeur
        
print("Le maximum dans la liste est :", max_val)
print("Le minimum dans la liste est :", min_val)
