# Liste de nombres arrondis
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
L_arrondis = [round(nombre) for nombre in L]
L_arrondis.sort()
print("Liste arrondie et triée :", L_arrondis)
