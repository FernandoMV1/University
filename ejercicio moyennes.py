def moyennes(M):
    moy1 = 0
    moy2 = 0
    moytot = []
    for i in range (len(M)):
        moy1 += M[i][i]
        moy2 +=M[i][len(M)-1-i]
    moy1 /= len(M)
    moy2 /= len(M)

    moytot.append(moy1)
    moytot.append(moy2)

