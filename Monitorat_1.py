def premiers(n):
    compteur = 0
    nombre = 2
    lst = []
    
    if n <= 0:
        return lst  
    
    while compteur < n:
        is_premier = True
        for i in range(2, int(nombre**0.5)+1):
            if nombre % i == 0:
                is_premier = False
                break
        if is_premier:
            lst.append(nombre)
            compteur +=1

        nombre += 1
    return lst


print(premiers(5))


                


