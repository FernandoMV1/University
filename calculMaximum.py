# Calcul d'un maximum sous contrainte dans une liste

##################################################
# Fonction calculant un maximum d'une liste de nombres supposés non-négatifs
def calculMaximum01(v):
	monMaximum = -1.0 # initialisation du maximum actuel à -1.0 (plus petit que tout nombre non-négatif et donc jamais maximum)
	for x in v: # boucle sur les éléments de v
		if x > monMaximum: # le nombre est-il plus grand que le maximum actuel
			monMaximum = x # si oui, il devient le nouveau maximum actuel
	return(monMaximum) # la fonction renvoie le maximum

##################################################
# Fonction calculant un maximum d'une liste de nombres
def calculMaximum02(v):
	monMaximum = v[0] # initialisation du maximum actuel à la valeur du premier élément
	for x in v: # boucle sur les éléments de v
		if x > monMaximum: # le nombre est-il plus grand que le maximum actuel
			monMaximum = x # si oui, il devient le nouveau maximum actuel
	return(monMaximum) # la fonction renvoie le maximum

##################################################
# Fonction calculant un maximum d'une liste de nombres
def calculMaximum03(v):
	monMaximum = v[0] # initialisation du maximum actuel à la valeur du premier élément
	for i in range(len(v)): # boucle sur les indices de v
		if v[i] > monMaximum: # le nombre est-il plus grand que le maximum actuel
			monMaximum = v[i] # si oui, il devient le nouveau maximum actuel
	return(monMaximum) # la fonction renvoie le maximum

##################################################
# Fonction calculant le maximum des nombres impairs d'une liste de nombres non-négatifs (maximum sous contrainte)
def calculMaximum04(v):
	monMaximum = -1.0 # initialisation du maximum actuel à -1
	for x in v: # boucle sur les éléments de v
		if x % 2 == 1:
			if x > monMaximum: # le nombre est-il plus grand que le maximum actuel
				monMaximum = x # si oui, il devient le nouveau maximum actuel
	return(monMaximum) # la fonction renvoie le maximum
##################################################
# Exemples
liste = [1, 3, 34, 2, 5, 10, 4, 11]

print(calculMaximum01(liste))
print(calculMaximum02(liste))
print(calculMaximum03(liste))
print(calculMaximum04(liste))
##################################################
