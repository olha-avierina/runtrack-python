# affishe tapis avec diagonale
def afficher_tapis_diagonalen(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j :
                print(" ", end="")
            else:
                print("#", end="")
        print()
afficher_tapis_diagonalen(10)
