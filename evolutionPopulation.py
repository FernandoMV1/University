# Calcul de l'évolution du nombre d'individus d'une population au cours du temps

##################################################
# Fonction 1 calculant l'évolution du nombre d'individus en fonction du temps
# La période de temps t_max ainsi que le nombre d'individus x0 et x1 au temps t=0 et t=1 sont donnés en argument
# On suppose que ce nombre d'individus se calcule selon x(t) = a1 * x(t-1) + a2 * x(t-2)
def calculEvolution01(t_max, x0, x1, a1, a2):
	x = [x0, x1] # initialisation de la liste
	for t in range(2, (t_max + 1)): # boucle sur toute la période de temps
		x_t = a1 * x[t-1] + a2 * x[t-2] # calcul de la population au temps t
		x.append(x_t) # ajouter à la liste
	return(x) # la liste calculée est renvoyée par la fonction

#################################################
# Fonction 2 calculant l'évolution du nombre d'individus en fonction du temps
def calculEvolution02(t_max, x0, x1, a1, a2):
	x = [0] * (t_max + 1) # création de la liste
	x[0] = x0
	x[1] = x1 # initialisation de la liste
	for t in range(2, (t_max + 1)): # boucle sur toute la période de temps
		x[t] = a1 * x[t-1] + a2 * x[t-2] # calcul de la population au temps t
	return(x) # la liste calculée est renvoyée par la fonction

##################################################
# Exemples
t_max = 10
x0 = 0
x1 = 100
a1 = +1.1
a2 = -0.2

print(calculEvolution01(t_max, x0, x1, a1, a2))
print(calculEvolution02(t_max, x0, x1, a1, a2))
