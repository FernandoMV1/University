#TP 3

def nbr_mot(string):
    mots = string.split()
    return len(mots)

########################################

def anagramme(str1, str2):
    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)

########################################

def change(str):
    return str.replace("r","l")

#######################################

def miroir(string):
    string = string[::-1]

    return string

######################################

def verifierMul(l,n):
    if n == 0:
        return True 
    
    for i in l:
        if i % n != 0:
            return False
        
    return True

#####################################

def merge_two_lists(lst1, lst2):
    lst1.extend(lst2)
    sorted_list = sorted(lst1)
    
    return sorted_list







