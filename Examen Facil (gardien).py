import math

def Arret(BUT):
    # Trouver les positions du ballon (B) et du gardien (G)
    H = len(BUT)    # Hauteur du but (nombre de lignes)
    L = len(BUT[0]) # Longueur du but (nombre de colonnes)
    
    # Initialiser les coordonnées
    gx = gy = bx = by = None
    
    # Parcourir la matrice pour trouver les positions du gardien (G) et du ballon (B)
    for i in range(H):
        for j in range(L):
            if BUT[i][j] == 'G':
                gx, gy = j, i  # Position du gardien (x, y)
            elif BUT[i][j] == 'B':
                bx, by = j, i  # Position du ballon (x, y)
    
    # Calcul de la direction
    if bx < gx:
        direction = -1.0  # Ballon à gauche
    elif bx > gx:
        direction = 1.0   # Ballon à droite
    else:
        direction = 0.0   # Ballon en face du gardien
    
    # Calcul de l'angle (en degrés)
    dx = bx - gx  # Différence horizontale (en pixels)
    dy = by - gy  # Différence verticale (en pixels)
    
    # Calcul de l'angle avec atan2
    angle = math.degrees(math.atan2(dy, dx))  # atan2 renvoie l'angle en radians, donc on le convertit en degrés
    if angle < 0:
        angle += 180  # Pour s'assurer que l'angle est dans [0, 180] (par rapport au sol)
    
    # Calcul de la distance
    distance = math.sqrt(dx**2 + dy**2)
    
    return [direction, angle, distance]

# Exemple d'utilisation
BUT = [
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'B'],
    ['G', 'X', 'X', 'X', 'X']
]

result = Arret(BUT)
print(result)


    
