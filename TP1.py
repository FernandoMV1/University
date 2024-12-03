def heure(secondes):
    heures = secondes // 3600
    minutes = (secondes % 3600) // 60
    secondes = secondes % 60
    print(f"{heures} heures, {minutes} minutes, {secondes} secondes")

heure(9999)

def moyenne (arg1, arg2):
    resultat = (arg1 + arg2)/2
    print(f"la moyenne est {resultat}")

moyenne(2,4)

def main():
    nombre1 = int(input("Entrez le premier nombre: "))
    nombre2 = int(input("Entrez le deuxieme nombre: "))
    moyenne(nombre1, nombre2)

main()

import math

def volume(r):
    return (4/3)* math.pi * r**3

def surface(r):
    return 4 * math.pi * r ** 2

def max():
    try:
        a = int(input("Entrez le numero 1 : "))
        b = int(input("Entrez le numero 2 : "))
        c = int(input("Entrez le numero 3 : "))
    except EOFError:
        # Si une erreur EOF est détectée, on utilise des valeurs par défaut
        a, b, c = -100, 6, -50

    # Comparaison pour trouver le plus grand nombre
    if a >= b and a >= c:
        max_nombre = a
    elif b >= a and b >= c:
        max_nombre = b
    else:
        max_nombre = c

    # Afficher le résultat du plus grand nombre
    print(f"Le nombre le plus grand est {max_nombre}")
    
    # Vérification des valeurs identiques
    if a == b or b == c or a == c:
        print("Mais vous avez introduit des valeurs identiques !")

# Appeler la fonction
max()

def amende(vmax, v):
    if v <= vmax:
        return 0
    elif vmax < v < (vmax + 10):
        amende_1 = (v - vmax) * 5
        amende_1 = max(amende_1, 12.5)
        return amende_1
    else:
        amende_1 = ((v - vmax) * 5) * 2
        return amende_1