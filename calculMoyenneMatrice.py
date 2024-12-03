# Calcul de la moyenne des lignes et des colonnes d'une matrice
# La fonction prend en argument une matrice qui contient les scores
# donnés par des personnes en testant 4 différentes limonades (enquête
# marketing). Il faut calculer la moyenne par personne et par soda

##################################################
# Fonction calculant les moyennes de ligne et de colonne
def calculMoyennes(scores):
	n_sodas = len(scores) # nombre de sodas
	n_persons = len(scores[0]) # nombre de personnes

	soda_mean = [0] * n_sodas # initialisation à 0
	person_mean = [0] * n_persons # initialisation à 0

	# Parcours des éléments de la matrice scores
	for soda in range(len(scores)):
		for person in range(len(scores[0])):
			soda_mean[soda] += scores[soda][person] / n_persons # adapte la moyenne
			person_mean[person] += scores[soda][person] / n_sodas # adapte la moyenne

	return(soda_mean, person_mean) # renvoie les moyennes

##################################################
# Exemple: une matrice qui contient les scores donnés
# par des personnes en testant 4 différentes limonades
# (enquête marketing). Les limonades sont en ligne et
# les personnes en colonne.
scores = [[3, 4, 5, 2, 1, 4, 3, 2, 4, 4],
          [2, 4, 3, 4, 3, 3, 2, 1, 2, 2],
          [3, 5, 4, 5, 5, 3, 2, 5, 5, 5],
          [1, 1, 1, 3, 1, 2, 1, 3, 2, 4]]

soda_m, person_m = calculMoyennes(scores)

print("Moyennes des sodas: ", soda_m)
print("Moyennes des personnes: ", person_m)
