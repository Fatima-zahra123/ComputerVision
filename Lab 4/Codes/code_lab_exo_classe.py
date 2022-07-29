import numpy as np
import cv2

#Définir une canvas de taille 300x300 px, 
#avec 3 canaux (R,G,B) et le  data type comme 8 bit unsigned integer
canvas = np.zeros((300,300,3), dtype ="uint8")



# dessiner des cercles blanc concentriques
# calculer le point central du canvas
# genérer des cercles en utilisant la boucle for 
# avec des valeurs définies en liste (range
# afficher le canvas
canvas = np.zeros((300,300,3), dtype ="uint8")
blanc = (255,255,255)
(centreX, centreY) = (canvas.shape[1]//2, canvas.shape[0]//2)

for r in range(0,175,25):
    cv2.circle(canvas, (centreX,centreY), r, blanc)

cv2.imshow("Cercles concentrics", canvas)
cv2.waitKey(0)


# Générer aléatoirement le rayon, le centre, et la couleur
# dessiner les cercles par une boucle for
canvas = np.zeros((300,300,3), dtype ="uint8")
for i in range(0, 25):
    radius = np.random.randint(5, high = 200)
    coleur = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt = np.random.randint(0, high = 300, size = (2,))
    cv2.circle(canvas, tuple(pt), radius, coleur, -1)
cv2.imshow("25 Cercle aleatoire", canvas)
cv2.waitKey(0)
