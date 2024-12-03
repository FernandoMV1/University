# Vérifier si un string est compris dans un string plus long

##################################################
# Fonction 1 vérifiant si un mot (string s1) est compris dans un mot ou phrase (string s2) plus long
def motDansString01(s1,s2):
	for n2 in range(len(s2) - len(s1) + 1): # parcourir toutes les positions utiles de s2
		# print(s2[n2:(n2 + len(s1))]) # imprime les valeurs (optionnel)
		if s1 == s2[n2:(n2 + len(s1))]: return(True) # vérifie si le string s1 est présent en position n2 de s2
	return(False) # si pas présent renvoie faux

##################################################
# Fonction 2 vérifiant si un mot (string s1) est compris dans un mot ou phrase (string s2) plus long
def motDansString02(s1,s2):
	for n2 in range(len(s2) - len(s1) + 1): # parcourir toutes les positions utiles de s2
		if estPresent(s1,s2,n2): return(True) # vérifie si le string s1 est présent en position n2 de s2
	return(False) # si pas présent renvoie faux

##################################################
# Fonction vérifiant si un mot (string s1) est compris en position n dans un mot ou phrase (string s2) plus long
# Utilisé dans motDansString02
def estPresent(s1,s2,n):
	for n1 in range(len(s1)): # boucle sur les indices du string s1
		if s1[n1] != s2[n + n1]: # détermine si le string s1 est présent en position n dans s2
			return(False) # si pas présent, alors renvoie faux
	return(True) # si présent, renvoie vrai

##################################################
# Fonction 3 vérifiant si un mot (string s1) est compris dans un mot ou phrase (string s2) plus long
def motDansString03(s1,s2):
	for n2 in range(len(s2) - len(s1) + 1): # parcourir toutes les positions utiles de s2
		# print() # imprime les résultats intermédiaires pour bien comprendre le code
		present = True # initialisation
		# déterminer si le string s1 est présent en position n2 dans s2
		for n1 in range(len(s1)): # boucle sur les indices des caractères de s1
			# print(s1[n1],s2[n2 + n1],end="  ") # imprime les résultats intermédiaires pour bien comprendre le code
			# print() # imprime les résultats intermédiaires pour bien comprendre le code
			if s1[n1] != s2[n2 + n1]: # ce caractère en position n1 de s1 n'est pas présent
				present = False # alors le string s1 n'est pas présent en position n2
		if present: return(present) # renvoie vrai s'il est présent en position n2
	return(False) # renvoie faux si s1 n'est présent dans aucune des positions n2 de s2

##################################################
# Exemples

string1 = "lion"
string2 = "Le lion est mort"

print(motDansString01(string1,string2))
print(motDansString02(string1,string2))
print(motDansString03(string1,string2))

string1 = "tigre"
string2 = "Le lion est mort"

print()
print(motDansString01(string1,string2))
print(motDansString02(string1,string2))
print(motDansString03(string1,string2))

string1 = "mort"
string2 = "Le lion est mort"

print()
print(motDansString01(string1,string2))
print(motDansString02(string1,string2))
print(motDansString03(string1,string2))

string1 = "Le"
string2 = "Le lion est mort"

print()
print(motDansString01(string1,string2))
print(motDansString02(string1,string2))
print(motDansString03(string1,string2))
