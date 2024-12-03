# Calcul de la distance Euclidienne entre deux vecteurs de même taille

##################################################
# Fonction 1 calculant la distance Euclidienne entre deux vecteurs de même taille
def calculDistance01(x,y):
	distance = 0.0 # initialisation
	somme = 0.0 # initialisation
	for n in range(len(x)): # boucle sur les indices du vecteur
		somme = somme + (x[n] - y[n])**2 # somme cumulée des différences des éléments de x et y (en dimension n) au carré
	distance = somme ** (1/2) # fonallement, on prend la racine carrée
	return(distance) # la fonction renvoie la distance calculée

##################################################
# Fonction 2 calculant la distance Euclidienne entre deux vecteurs de même taille
def calculDistance02(x,y):
	distance = 0.0 # initialisation
	somme = 0.0 # initialisation
	n = 0 # initialisation
	while n < len(x): # boucle sur les indices du vecteur
		somme = somme + (x[n] - y[n])**2 # somme cumulée des différences des éléments de x et y (en dimension n) au carré
		n = n + 1 # incrémentation du compteur
	distance = somme ** (1/2) # fonallement, on prend la racine carrée
	return(distance) # la fonction renvoie la distance calculée

##################################################
# Fonction 3 calculant la distance Euclidienne entre deux vecteurs de même taille
from math import sqrt

def calculDistance03(x,y):
	distance = 0.0 # initialisation
	somme = 0.0 # initialisation
	n = 0 # initialisation
	while n < len(x): # boucle sur les indices du vecteur
		somme = somme + (x[n] - y[n])**2 # somme cumulée des différences des éléments de x et y (en dimension n) au carré
		n = n + 1 # incrémentation du compteur
	distance = sqrt(somme) # fonallement, on prend la racine carrée
	return(distance) # la fonction renvoie la distance calculée

##################################################
# Exemples
u = [1, 3, 2, 5, 10, 4]
v = [2, 0, 4, 5, -1, 1]

print(calculDistance01(u,v))
print(calculDistance02(u,v))
print(calculDistance03(u,v))
