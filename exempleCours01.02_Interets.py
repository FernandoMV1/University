# Exemple 2 du cours 1
# Epargne: calcul d'interets simples et composes

# Initialisation
i = 0.1 # interet sur un an (10%)
capital = 1000.0 # capital emprunte (en euro)
n = 6 # nombre d'annees

##################################################
# Calcul interet simple
Is = (i * capital) * n
print("Is =", Is)

# Valeur acquise interet simple
Cs = capital + Is # interet simple
print("Cs =", Cs)

##################################################
# Valeur acquise interet compose
Cc = capital       # au temps 0
Cc = Cc + (i * Cc) # au temps 1
Cc = Cc + (i * Cc) # au temps 2
Cc = Cc + (i * Cc) # au temps 3
Cc = Cc + (i * Cc) # au temps 4
Cc = Cc + (i * Cc) # au temps 5
Cc = Cc + (i * Cc) # au temps 6
print("Cc1 =", Cc)

# Calcul équivalent, valeur acquise interet compose
# On applique la formule la calculant
Cc = capital * ((1 + i)**n) # interet compose
print("Cc2 =", Cc)

# Calcul équivalent, valeur acquise interet compose
# On applique une boucle for itérative qui sera vue plus tard (cours 3)
Cc = capital           # au temps 0
for temps in range(1,n+1): # boucle itérative
    Cc = Cc + (i * Cc) # au temps 1 à n
print("Cc3 =", Cc)

##################################################
# Le capital composé est-il plus élevé que le capital simple ?
question = (Cc > Cs) # Cc > Cs ?
print("Cc > Cs ?", question)
