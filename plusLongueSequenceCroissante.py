# Plus longue sous-séquence strictement croissante dans une séquence donnée

##################################################
# Fonction 1 calculant la longueur de la plus longue sous-séquence strictement croissante dans une séquence,
# par exemple des températures évoluant dans le temps
def sousSequenceCroissante01(v):
	longueurMax = 0 # initialisation
	longueurActuelle = 0 # initialisation
	for i in range(len(v) - 1): # parcourir toutes les positions de v sauf la dernière
		if v[i+1] > v[i]: # si strictement croissant
			longueurActuelle += 1 # on augmente la longueur croissante
			if longueurActuelle > longueurMax: longueurMax = longueurActuelle # update la longueur maximale
		else:
			longueurActuelle = 0 # remise à 0 de la longueur actuelle
	return(longueurMax + 1) # renvoie la longueur maximale

##################################################
# Exemples
liste = [1, 3, 10, 34, 2, 5, 1, 2, 0, 4, 5, 8, 11]

print(sousSequenceCroissante01(liste))
##################################################
