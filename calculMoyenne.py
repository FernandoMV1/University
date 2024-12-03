# Calcul de la moyenne et de la moyenne sous contrainte

##################################################
# Fonction 1 calculant une moyenne
def calculMoyenne01(v):
	somme = 0.0 # initialisation
	n = 0 # initialisation
	for x in v: # boucle sur les éléments de v
		somme = somme + x # somme cumulée des éléments
		n = n + 1 # comptabilise  le nombre d'éléments
	moyenne = somme / n # calcule la moyenne
	return(moyenne) # renvoie la moyenne

##################################################
# Fonction 2 calculant une moyenne
def calculMoyenne02(v): # boucle sur les éléments de v
	somme = 0.0 # initialisation
	n = 0 # initialisation
	while n < len(v):
		somme = somme + v[n] # somme cumulée des éléments
		n = n + 1 # comptabilise  le nombre d'éléments
	moyenne = somme / n # calcule la moyenne
	return(moyenne) # renvoie la moyenne

##################################################
# Fonction 3 calculant une moyenne
def calculMoyenne03(v):
	somme = 0.0 # initialisation
	n = len(v) # calcul du nombre d'éléménts de v
	for x in v: # boucle sur les éléments de v
		somme = somme + x # somme cumulée des éléments
	return(somme/n) # renvoie la moyenne

##################################################
# Fonction 4 calculant une moyenne
def calculMoyenne04(v):
	somme = 0.0 # initialisation
	n = len(v) # calcul du nombre d'éléménts de v
	for i in range(n): # boucle sur les éléments de v
		somme = somme + v[i] # somme cumulée des éléments
	return(somme/n) # renvoie la moyenne

##################################################
# Fonction 5 calculant la moyenne des nombres pairs (moyenne sous contrainte)
def calculMoyenne05(v):
	somme = 0.0 # initialisation
	n = 0 # initialisation
	for x in v: # boucle sur les éléments de v
		if x % 2 == 0: # sélectionne les valeurs paires
			somme = somme + x # somme cumulée des éléments pairs
			n = n + 1 # comptabilise  le nombre d'éléments pairs
	moyenne = somme / n # calcule la moyenne
	return(moyenne) # renvoie la moyenne

##################################################
# Exemples
liste = [1, 3, 2, 5, 10, 4]

print(calculMoyenne01(liste))
print(calculMoyenne02(liste))
print(calculMoyenne03(liste))
print(calculMoyenne04(liste))
print(calculMoyenne05(liste))
