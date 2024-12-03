# Calcul du capital total lorsqu'on place un capital initial pendant une période de temps

##################################################
# Fonction calculant le capital total (en euro) lorsqu'on place un capital initial c
# en période (année) 0 pendant un durée de n années, avec un taux d'intérêt annuel de t%
def epargne(c, t, n):
	i = t/100 # taux d'intérêt
	capital_compose = c # initialisation du capital actuel
	for mois in range(1, n+1): # boucle sur toutes les périodes (mois)
		capital_compose = capital_compose + i * capital_compose # capital actuel augmenté des intérêts
		print(mois, capital_compose) # impression des résultats intermédiaires
	return(capital_compose) # renvoie le capital composé final

##################################################
# Exemples

capital = 1000 # en euros
taux_annuel = 10 # en pourcents
duree = 6 # en années

print(epargne(capital, taux_annuel, duree))
