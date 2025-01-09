#ex1
def jourSansPluie(x):
    compteur = 0
    for jour in range(len(x)-1):
        if x[jour] == 0.0:
            copteur += 1
    return compteur

def ecarType(x):
    somme = 0
    sd = 0
    n = len(x)
    for i in range(n):
        somme += x[i]

    moyenne = somme / n
    for i in range(n):
        var += (1/n)*(x[i] - moyenne)**2
        sd = (var)**(1/2)
    return sd

def analyse(Pays):
    max_1 = 0
    max_2 = 0
    Resultat = {}
    for key, value in Pays.items():
        if jourSansPluie(value) > max_1:
            max_1 = jourSansPluie(value)
            Resultat["nbreJours"] = key
        if ecarType(value) > max_2:
            max_2 = ecarType(value)
            Resultat["nbreJours"] = key

########################################################
#ex2

def domine(x,y,sens):
    x_domine = False
    max = -1
    min = 100000000000000000000000000
    for i in range(len(x)):
        if sens[i]==1:
            if x[i] > y[i]:
                x_domine = True
            if x[i] < y[i]:
                return False
        elif sens[i]== -1:
            if x[i] < y[i]:
                x_domine = True
            if x[i] > y[i]:
                return False
    return x_domine

def gagnant(Resultats, sens):
    n = len(Resultats)
    for i in range(n):
        est_dominant = True
        for j in range(n):
            if i != j:
                if not domine(Resultats[i],Resultats[j],sens):
                    est_dominant = False
                    break
        if est_dominant:
            return i
    return -1

###############################################################################

def transposition(grille):
    grille_t = []
    n = len(grille)
    m = len(grille[0])
    for i in range(m):
        palabra = ""
        for t in range(n):
            palabra += grille[i][t]
        grille_t.append(palabra)
    return grille_t

def palabraenfila(filamat, palabra):
    for fila in filamat:
        if filamat.find(palabra) != -1:
            return True
    return False

def caracteres(grille):
    filamat = []
    for i in range(len(grille)):
        letras = ""
        for f in range(len(grille[i])):
            letras += grille[i][f]
        filamat.append(letras)
    return filamat

def motCache(grille, mot):
    filamat = caracteres(grille)
    grille_t = transposition(filamat)
    if (len(mot)>len(grille)) and (len(mot) > len(grille[0])):
        return False
    if palabraenfila(filamat, mot) or palabraenfila(grille_t, mot):
        return True
    return False

##########################################################################

#examen janvier 2021
def trouver_pairs(no_telephones):
    l = []
    for pers1, num1 in no_telephones.items():
        for pers2, num2 in no_telephones.items():
            if num1 == num2:
                    if pers1 != pers2:
                        if [pers1, pers2] not in l:
                            if [pers2, pers1] not in l:
                                l.append([pers1,pers2])
    return l

def moy_personnes(no_telephones):
    d = {}
    for valor in no_telephones.values():
        if valor not in d:
            d[valor] = 1
        else:
            d[valor] += 1

    for i in d:
        somme += d[i]

    moyenne = somme/len(d)
    return moyenne

####################################################################
def moy_diag(M):
    somme1 = 0
    somme2 = 0
    for i in range(len(M)):
        somme1 += M[i][i]
        somme2 += M[i][len(M)-i-1]

    d1 = somme1/len(M)
    d2 = somme2/len(M)

    return d1, d2

def est_maximun_local(M, i, j):
    x = M[i][j]

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            if M[i+di][j+dj] >= x:
                return False
    return True

def maxima(M):
    coord = []
    for i in range(1, len(M)-1):
        for j in range(1, len(M[0]-1)):
            if est_maximun_local(M, i, j):
                coord.append([i, j])
    return coord

#######################################################################
#Aout 2022
def moyenne_cours(M):
    l_cours = [0]*(len(M[0])-1)

    for notes in range(2, len(M)):
        for cours in range(1, len(M[0])):
            l_cours[cours-1] += M[notes][cours]/(len(M)-2)
    return l_cours

def moyenne_etudiant(M):
    l_notes = [0] * (len(M) - 2)
    somme_credits = 0.0
    for cours in range(1, len(M[0])):
        somme_credits += M[1][cours]
        for notes in range(2, len(M)):
            l_notes[notes-2] += (M[1][cours] * M[notes][cours])/somme_credits

    return l_notes

def minmax_etudiant(M):
    id_max = None
    id_min = None
    max = -1
    min = 1000000000000000000000
    moyenne = moyenne_etudiant(M)
    for i in range(len(moyenne)):
        if moyenne[i] > max:
            id_max = M[i+2][0]
        if moyenne[i] < min:
            id_max = M[i+2][0]
    return id_max, id_min

#########################################################################################

def Ajour_Volume(Dico_Ref):
    Dico_Ref_Modifier = {}
    for key, val in Dico_Ref.items():
        volume = val[0] * val[1] *val[2]
        val.append(volume)
        Dico_Ref_Modifier[key] = val
    return Dico_Ref_Modifier

def Tri_Colis(Liste_Ref_Colis, Dico_Ref_Modifier): #Tri a bulles
    n = len(Liste_Ref_Colis)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            current_vol = Dico_Ref_Modifier[Liste_Ref_Colis[j]][-1]
            next_vol = Dico_Ref_Modifier[Liste_Ref_Colis[j+1]][-1]
            if current_vol < next_vol:
                Liste_Ref_Colis[j], Liste_Ref_Colis[j+1] = Liste_Ref_Colis[j+1], Liste_Ref_Colis[j]
                swapped = True

        if not swapped:
            break
    return Liste_Ref_Colis

def Chargement_Camions(Liste_Colis_Tries, Volume_Camion, Dico_Ref_Modifie):
    l = []
    somme_vol = 0
    compteur = 0
    for colis in Liste_Colis_Tries():
        volume_colis = Dico_Ref_Modifie[colis][-1]
        if somme_vol + volume_colis < Volume_Camion:
            somme_vol += volume_colis
        else:
            compteur += 1
            l.append(Liste_Colis_Tries(colis))
#Incomplet
#########################################################################################################
#Janvier 2022
def trajectoire(M, x_start, y_start):
    compteur = 0
    x, y = x_start, y_start
    while True:
        coord_start = M[x][y]
        voisins = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        min_coord = coord_start
        meilleur_voisin = None
        for (dx, dy) in voisins: #prend la coordonnée la plus petite voisine pour apres se deplacer
            if 0 <= dx < len(M) and 0 <= dy < len(M[0]):
                if M[dx][dy] < min_coord:
                    meilleur_voisin = (dx, dy)
                    min_coord = M[dx][dy]
        if meilleur_voisin: # parcours la matrice
            x, y = meilleur_voisin
            compteur += 1
        else:
            break
    return [compteur, (x, y)]

#####################################################################################################
def transformer_liste(liste_ref, dico_rayon):
    l = []
    for i in liste_ref:
        parties = i.split("#")
        for k in dico_rayon:
            if parties[0] == k:
                rayon = dico_rayon[k]
                break

        if rayon is not None:
            l.append([rayon, int(parties[1]), int(parties[2])])
    return l

def representer_carte(carte_supermarche, dico_rayon, liste_ref, p):
    carte_reapp = [[0 for i in range(len(carte_supermarche[0]))] for j in range(len(carte_supermarche))]
    liste_trans = transformer_liste(liste_ref, dico_rayon)
    for rayon, etal, quantite in liste_trans:
        produit_actuel = carte_supermarche[rayon][etal]
        produit_manquant = p - produit_actuel
        if produit_manquant > 0:
            if produit_manquant < int(quantite):
                a_ajouter = produit_manquant
            else:
                a_ajouter = int(quantite)

            carte_reapp[rayon][etal] = a_ajouter
    return carte_reapp


############################################################################
def tridebulles(l):
    for i in range(len(l)):
        swapped = False
        for j in range(0, len(l)-i-1):
            if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if not swapped:
            break
    return l
###########################################################################
'''

EXAMEN DIFICILES

'''
def verifierDiagonales(M):
    somme1 = 0
    somme2 = 0
    for i in range(len(M)):
        somme1 += M[i][i]
        somme2 += M[i][len(M)-i-1]
        if somme1 == somme2:
            return False
        else:
            return True
        
def verifierLignes(M):
    l = [0 for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            l[i] += M[i][j]
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] == l[j]:
                return False
    return True

def verifierColonnes(M):
    l2 = [0 for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            l2[j] += M[i][j]
    for i in range(len(l2)):
        for j in range(len(l2)):
            if i != j and l2[i] == l2[j]:
                return False
    return True

######################################################################
class Casier:
    def __init__(self, bac):
        self.__bac = bac

    def party(self, nom):
        for i in range(self.__bac):
            for j in range(self.__bac[0]):
                biere = self.__bac[i][j]
                if biere.getNom() == nom and biere.estPleine():
                    biere.boire()

    def avgAlcool(self):
        somme_alcool = 0
        compteur_biere = 0
        for i in range(self.__bac):
            for j in range(self.bac[0]):
                biere = self.__bac[i][j]
                if biere.estPleine():
                    somme_alcool += biere.getAlcool()
                    compteur_biere += 1
        moyenne_alcool = somme_alcool/compteur_biere
        return moyenne_alcool
    
    def isStronger(self, tab):
        taux = self.avgAlcool()
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                if tab[i][j] > taux:
                    return False
                return True
#####################################################################
def ProbabilityMatrix(A):
    P = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    dout = OutdegreeVector(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            P[i][j] = A[i][j] / dout[j]
    return P

def ProduitMatriceVecteur(P,d):
    valeur = [0 for j in range(len(P))]
    if len(P[0]) == len(d):
        for i in range(len(P)):
            for j in range(len(P[0])):
                valeur[i] += P[i][j]*d[j]
    return valeur

from math import *
def converge(x, y):
    somme = 0
    for i in range(len(x)):
        somme += abs(y[i] - x[i])
        if somme < 0.000001:
            return True
        return False
    
def normaliser(V):
    somme = 0
    sortie = [0 in range(len(V))]
    for i in V:
        somme += i
    for i in range(len(V)):
        sortie[i] = V[i]/somme
    return sortie

def PageRankedScore(A):
    P = ProbabilityMatrix(A)
    Pt = Transpose(P)
    din0 = normaliser(IndegreeVector(A))
    din1 = normaliser(ProduitMatriceVecteur(P,din0))
    while not converge(din0, din1):
        din0 = din1
        din1 = normaliser(ProduitMatriceVecteur(P,din0))
    return din1

#############################################################
def maximaLocaux(tab):
    l = []
    for i in range(1, len(tab)-1):
        if (tab[i] > tab[i-1]) and (tab[i] > tab[i+1]):
            l.append(tab[i])
    return l

def estValle(tab, a, b):
    Valle = True
    for i in range(a, b+1):
        if (tab[i] > valeurDroite(a, tab[a], b, tab[b], i)):
            Valle = False
        return Valle

def plusGrandeVallee(tab):
    tabmax = maximaLocaux(tab)
    resultat =[]
    debut, fin, longueurPlusGrandVallee = 0, 0, 0
    for i in range(0, len(tabmax)):
        for j in range(i+1, len(tabmax)):
            if (estValle(tab, maximaLocaux[i], maximaLocaux[j]) and abs(maximaLocaux[j] - maximaLocaux[i]) > longueurPlusGrandVallee):
                debut = maximaLocaux[i]
                fin = maximaLocaux[j]
                longueurPlusGrandVallee = abs(maximaLocaux[j] - maximaLocaux[i])

###############################################################################################################################################
#Tri de bulles avec format spécifique
def tribulles(l):
    for i in range(len(l)):
        swapped = False
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if not swapped:
            break
    resultat = ''
    for i in l:
        if i == len(l) -1: 
            resultat += str(i) +  ''
        else:
            resultat += str(i) + ' '
    print(resultat)

####################################################
#Ajour prenom
def ajoutPrenom(liste, prenom):
    for i in liste:
        if prenom in i:
            return liste
    if not liste:
        liste.append(prenom)
    else:           
        for i in range(len(liste)):
            if prenom < liste[i]:
                liste.insert(i, prenom)
                break
            else:
                liste.append(prenom)
###################################################
#mx matrice:
def maxmatrice(mat):
    max_val = -10000000
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > max_val:
                max_val = mat[i][j]
    return max_val
##################################################
#Fibonacci
def fibo(n):
    f0 = 0
    f1 = 1
    if n == 0 or n < 0:
        return f0
    for i in range(2, n+1):
        f0, f1 = f1, f0 + f1
    return f1
print(fibo(1))
####################################################
#Trasposer un matrice
def trasposer(M):
    Mt = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            Mt[j][i] = M[i][j]
    return Mt
##########################################################
#Carre magique
def estMagique(mat):
    somme_lignes = [0 for i in range(len(mat))]
    somme_colonnes = [0 for i in range(len(mat[0]))]
    somme_diagonales = [0,0]
    if len(mat) != len(mat[0]):
        return False
    for i in range(len(mat)): #calcule lignes et colonnes
        for j in range(len(mat)):
            somme_lignes[i] += mat[i][j]
            somme_colonnes[i] += mat[j][i]
        somme_diagonales[0] += mat[i][i]
        somme_diagonales[1] += mat[i][len(mat)-i-1]
        
    ref = somme_lignes[0]
    for i in range(1, len(somme_lignes)):
        if ref != somme_lignes[i]:
            return False
    for i in range(len(somme_colonnes)):
        if ref != somme_colonnes[i]:
            return False
    if somme_diagonales[0] != ref or somme_diagonales[1] != ref:
        return False
    return True
#########################################################################
#Verifier les nombres premiers 
def est_premier(x):
    if x < 2:
        return False
    for i in range(2, int((x)**(1/2)) + 1):
        if x % i == 0:
            return False
    return True

def premiers(n):
    l = []
    if n <= 0:
        return l
    compteur = 2
    while len(l) < n:
        if est_premier(compteur):
            l.append(compteur)
            compteur += 1
    return l
###############################################################
#distance euclidienne matrice
def dist_euclidienne_indiv(M):
    nb_indv = len(M)
    nb_carac = len(M[0])
    m = [[0 for i in range(nb_indv)] for j in range(nb_indv)]
    
    for i in range(nb_indv):
        for j in range(nb_indv):
            somme = 0
            for k in range(nb_carac):
                somme += (M[i][k] - M[j][k])**2
                m[i][j] = (somme)**(1/2)
    return m
#################################################################
#similitude des mots
def to_dic(doc):
    message = doc.split()
    dic = {}
    for mot in message:
        if mot in dic:
            dic[mot] += 1
        else:
            dic[mot] = 1
    return dic

def similaire(doc1, doc2, listes_mots):
    dic1 = to_dic(doc1)
    dic2 = to_dic(doc2)
    compteur = 0
    for mot in listes_mots:
        if mot in dic1 and mot in dic2:
            if dic1[mot] == dic2[mot]:
                compteur += 1
    if compteur/len(listes_mots) < 0.8:
        return False
    return True
######################################################
#Classe Bibliotheque
class Document:
    def __init__(self, auteurs, titre):
        self.__auteurs = auteurs
        self.__titre = titre
        self.__nb_exemplaire = 1
        self.__nb_exemplaire_present = 1

    def get_auteurs(self):
        return self.__auteurs
    def get_titres(self):
        return self.__titres
    def get_nombre_exemplaire(self):
        return self.__nb_exemplaire
    def get_nombre_exemplaire_restant(self):
        return self.__nb_exemplaire_present
    
    def est_present(self):
        if self.__nb_exemplaire_present < 1:
            return False
        return True
    def emprunt(self):
        if self.__nb_exemplaire_present > 1:
            self.__nb_exemplaire_present -= 1
            return "Ok"
        return "Impossible"
    def retour(self):
        if self.__nb_exemplaire_present < self.__nb_exemplaire:
            self.__nb_exemplaire += 1
            return "Ok"
        return "Impossible"
    def ajout(self):
        self.__nb_exemplaire += 1
    def supression(self):
        if self.__nb_exemplaire_present == self.__nb_exemplaire:
            self.__nb_exemplaire = 0
            self.__nb_exemplaire_present = 0
            return "Ok"
        return "Impossible"

class Livre(Document):
    def __init__(self, auteurs, titre, nombre_pages, genre, date):
        super().__init__(auteurs, titre)
        self.__nombre_pages = nombre_pages
        self.__genre = genre
        self.__date = date

    def get_nombre_pages(self):
        return self.__nombre_pages
    def get_genre(self):
        return self.__genre
    def get_date(self):
        return self.__date
    
class Article(Document):
    def __init__(self, auteurs, titre, sources, sujet, date):
        super().__init__(auteurs, titre)
        self.__nombre_sources = len(sources)
        self.__sujet = sujet
        self.__date = date

    def get_sources(self):
        return self.__nombre_sources
    def get_sujet(self):
        return self.__sujet
    def get_date(self):
        return self.__date

class Periodique(Document):
    def __init__(self, auteurs, titre, sujets, date_debut, date_fin):
        super().__init__(auteurs, titre)
        self.__sujets = sujets
        self.__nombre_sujets = len(sujets)
        self.__date_debut = date_debut
        self.__date_fin = date_fin

    def get_sujets(self):
        return self.__sujets
    def get_nombre_sujets(self):
        return self.__nombre_sujets
    def get_date_debut(self):
        return self.__date_debut
    def get_date_fin(self):
        return self.__date_fin
    








    

















                    








        