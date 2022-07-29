import numpy as np
import cv2

#Définir une canvas de taille 300x300 px, avec 3 canaux (R,G,B) et le  data type comme 8 bit unsigned integer
canvas = np.zeros((300,300,3), dtype ="uint8")


#Définir le code de couleur vert
#Tracer la ligne paramètres : dans canvas (ou image), du point (0,0) vers le point (300,300), comme couleur "vert« 
#Afficher l’image/canvas 

vert = (0,255,0)
cv2.line(canvas,(0,0),(300,300),vert)
cv2.imshow("La ligne 1", canvas)
cv2.waitKey(0)

# Déssiner une ligne avec une épaisseur 
rouge = (0,0,255)
cv2.line(canvas,(0,0),(300,300),rouge, 3)
cv2.imshow("La ligne 2", canvas)
cv2.waitKey(0)

#Déssiner un réctangle
vert = (0,255,0)
cv2.rectangle(canvas,(10,10),(60,60),vert)
cv2.imshow("Le rectangle 1", canvas)
cv2.waitKey(0)

rouge = (0,0,255)
cv2.rectangle(canvas,(10,10),(60,60),rouge, 3)
cv2.imshow("Le rectangle 2", canvas)
cv2.waitKey(0)

bleu = (255,0,0)
cv2.rectangle(canvas,(10,10),(60,60),bleu, -1)
cv2.imshow("Le rectangle 3", canvas)
cv2.waitKey(0)
#Dessin de cercle
#Définir un autre canvas pour déssiner un cercle 
canvas2 = np.zeros((300,300,3), dtype ="uint8")
#Définir un code de couleur 
#Tracer un cercle avec paramètres : dans canvas (ou image), 
#le centre (100,100) ,comme couleur "couleur", l'épaisseur est optionnelle  
#Afficher l’image/canvas 

couleur = (100,255,100)
cv2.circle(canvas2,(100,100), 50, couleur)
cv2.imshow("Single circle", canvas2)
cv2.waitKey(0)