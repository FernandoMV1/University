def demiSomme(mat):
    if len(mat) != len(mat[0]):
        return None
    lst = []
    for i in range(len(mat)):
        somme = 0
        for j in range(len(mat)):
            if j >= i:
                somme += mat[i][j]
        lst.append(somme)
    return lst

#######################################################################

def estMagique(mat):
    if len(mat) != len(mat[0]):
        return False
    sum1,sum2,sumref = 0,0,0

    for i in range(len(mat)):
        sum1 += mat[i][i]
        sum2 += mat[len(mat)-1-i]

    if sum1 != sum2:
        return False
    sumref = sum1

    for i in range (len(mat)):
        sum1,sum2 = 0,0
        for j in range(len(mat)):
            sum1 += mat[i][j]
            sum2 += mat[j][i]
        if ((sum1 != sumref) or (sum2 != sumref)):
            return False
    return True

#######################################################################
def payetaxi(m,p):
    record = 0
    total = 0
    n_record =[]
    if m == []:
        n_record = 0
    
    for i in range(len(m)):
        xa = m[i][1]
        ya = m[i][2]
        xb = m[i][3]
        yb = m[i][4]
        distance = abs(xb-xa)+abs(yb-ya)
        gain = p*distance
        if record < gain:
            record = gain
            n_record = m[i][0]

        total += gain
    return [total, n_record]

m = []



###############################################

def meteo(lst1,lst2):
    output = []
    for i in range(len(lst1)):
        output.append([0]*len(lst1))
       
    for lin in range(len(lst1)):
        for col in range(len(lst1)):
            pos = lst1[lin][col]
            valeur = lst2[lin][col]
            output[pos[0]][pos[1]]=valeur
           
    return output
        

