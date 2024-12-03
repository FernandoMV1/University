def nombreVoisinsVivants(etatActuel, x, y):
    directions = [(-1,0,1)]
    vivants = 0
    for nx in directions:
        for ny in directions: #Iteration sur les déplacements possibles dans la matrice
            if not (nx==0 and ny==0): #exclure la caisse centrale d'etre comptée comme voisine
                if etatActuel[nx+x][ny+y] == True:
                    vivants += 1


