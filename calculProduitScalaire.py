# Calcul du produit scalaire entre deux vecteurs de même taille

##################################################
# Fonction 1 calculant le produit scalaire entre deux vecteurs de même taille
def produitScalaire01(x,y):
	ps = 0.0 # initialisation
	for n in range(len(x)): # calcul du produit scalaire entre les vecteurs x et y
		ps = ps + x[n] * y[n] # somme cumulée des produits des éléments de x et y (en dimension n)
	return(ps) # renvoie le produit scalaire

##################################################
# Fonction 2 calculant la distance Euclidienne entre deux vecteurs de même taille
def produitScalaire02(x,y):
	ps = 0.0 # initialisation
	n = 0 # initialisation
	while n < len(x): # calcul du produit scalaire entre les vecteurs x et y
		ps = ps + x[n] * y[n] # somme cumulée des produits des éléments de x et y (en dimension n)
		n = n + 1 # incrémente l'indice de position
	return(ps) # renvoie le produit scalaire

##################################################
# Exemples
u = [1, 3, 2, 5, 10, 4]
v = [2, 0, 4, 5, -1, 1]

print(produitScalaire01(u,v))
print(produitScalaire02(u,v))
