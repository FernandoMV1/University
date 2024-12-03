#On definit notre fonction
def nbr_mots(string):
    compteur = 0 #conter les mots
    x = " " #Conter les caracteres
    is_car_previous = False #Il y a un caractere avant?

    for i in range(len(string)):
        x = string[i] #On parcours le string pour chaque caractere

        if x != " ":
            is_car_previous = True #si x n'est pas vide, alors il a un caractere

        elif (x == " ") and is_car_previous:
            compteur += 1
            is_car_previous = False

    x == string[len(string)-1]
    if x != " ":
        compteur += 1 #On verifie que le dernier mot soit compter car il n'y a pas d'espace a la fin
    return compteur

######################################################################################################################
                       
def anagramme(str1, str2):
    if len(str1) != len(str2):
        return False
    
    else:
        compteur = 0 #On va conter les lettres en commun
        for i in range(len(str1)):
            if str1[i] in str2:
                compteur +=1

        if (len(str1) == compteur):
            return True
        else:
            return False

######################################################################################################################

def changer(str):
    new_str = "" #comme les chaine de caractere ne sont pas muttables on doit creer une autre
    for i in range(len(str)):
        if str[i] == "r":
            new_str += "l"
        else:
            new_str += str[i]
    return new_str

######################################################################################################################

def miroir(mot):
    new_mot = ''
    for i in range(len(mot)-1,-1, -1):
        new_mot += mot[i]

    return new_mot
        

######################################################################################################################

def verifierMul(l,n):
    for i in l:
        if i % n != 0:
            return False
        else:
            return True
    
l = [0,7,14,21]

######################################################################################################################

def merge_two_lists(lst1, lst2):
    if lst1 == []:
        return lst2
    elif lst2 == []:
        return lst1
    else:
        lst3 = []
        i = 0
        j = 0
        fin = False
        while not fin:
            if lst1[i] < lst2[j]:
                lst3.append(lst1[i])
                i += 1
            elif lst1[i] == lst2[j]:
                lst3.append(lst1[i]) 
                i += 1
                j += 1
            else:
                lst3.append(lst2[j])
                j += 1

            if len(lst1) == i:
                lst3.extend(lst2[j:])
                fin = True
            elif len(lst2) == j:
                lst3.extend(lst1[i:])
                fin = True

    return lst3

lst1 = [1,3,5,7,8,8]
lst2 = [2,4,6,8]
print(merge_two_lists(lst1, lst2))

######################################################################################################################

def tribulles(l):
    for i in range(len(l)-1,-1,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = l[j]
    for i in range(len(l)):
        print(l[i], end = " ")
        print()
