#Tp2

def pair(nbr):
    if nbr <= 1:  
        return 0

    somme = 0  
    for i in range(2, nbr, 2):  
        print(i, end=" ")  
        somme += i 

    print() # retourner a la ligne a la fin
    return somme 
pair(20)

#######################################################################################

def carre(n):
    for i in range(n):
        for j in range(n):
            print ("*", end = " ")
        print()
carre(8)  

#######################################################################################

def triangle1(n):
    for i in range(1, n+1):
        for j in range(i):
            print ("*", end = " ")
        print()
triangle1(8) 

#######################################################################################

def triangle2(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end = " ")
        for k in range (i):
            print("*", end = " ")
        print()

triangle2(5)

#######################################################################################

#Pas du TP mais interessant a savoir
def triangle3(n):
    for i in range(n+1, 1, -1):
        for j in range(i):
            print ("*", end = "")
        print()
triangle3(8)

#######################################################################################

def fact(n):
    if n < 0:  
        return None
    elif n == 0:  
        return 1  
    
   
    resultat = 1
    for i in range(1, n + 1):  
        resultat *= i  

    return resultat  

#######################################################################################

def fibo(n):

    if n == 1:
        return 1
    if n <= 0:
        return 0
    
    a = 0 #F0
    b = 1 #F1

    for i in range(2, n+1):
        resultat = a + b 
        a = b
        b = resultat  
    return b
print(fibo(5))

###################################################

def distance(m):
    if m <= 0:
        return 0
    
    terre_lune = 384400000000
    nbr_doublage = 0
    
    while m < terre_lune:

        m = m * 2
        nbr_doublage += 1

    return nbr_doublage