from math import *
def trajectoire(mat):
    x=0
    nbrediagonales = 0
    while mat[x][0]!=1:
        x+=1
    for y in range(1,len(mat[0])):
        if x<len(mat)-1 and mat[x+1][y]==1:
            nbrediagonales += 1
            x += 1
        elif x>0 and mat[x-1][y]==1:
            nbrediagonales += 1
            x -= 1

    return sqrt(2)*nbrediagonales + len(mat[0])-1-nbrediagonales
