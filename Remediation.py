def s(mot_de_passe):
    lst = ['!','@','#','%','&','*']
    for i in lst:
            if i in mot_de_passe:
                return True
    return False        

def contient_majuscule(mot_de_passe):
    for maj in mot_de_passe:
          if "A" <= maj <= "Z":
               return True
    return False

def contien_quatre_chiffres(mot_de_passe):
     chiffres = [str(j) for j in range(10)]
     compteur_ch = 0
     for ch in mot_de_passe:
        if ch in chiffres:
            compteur += 1
     return compteur_ch >= 4
     
def saisir_mot_de_passe(taille_min):
    compteur = 0
    correct = False

    while not correct:

        mot_de_passe = input("Entrez un mot de passe: " )

        if len(mot_de_passe) < taille_min:
            print("Erreur1" )
            correct = False

        if not s(mot_de_passe):
             print("Erreur2")
             correct = False

        if not contient_majuscule(mot_de_passe):
             print("Erreur3")
             correct = False
    

        if not contien_quatre_chiffres(mot_de_passe):
             print("Erreur4")
             correct = False
             
                  

        
            
        
        




        compteur += 1








