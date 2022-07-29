#import argparse
from msilib.schema import Media
import cv2


# Récupération des arguments and save in dictionary
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Entrez le chemin de l'image")
args = vars(ap.parse_args())
"""

# Chargement et convertion de l'image en tableau numpy array
# Affichage des caractérisrtiques 
image = cv2.imread("fleurs.jpg")
print("La largeur de l'image en pixels est: {}".format(image.shape[1]))
print("La hauteur de l'image en pixels est: {}".format(image.shape[0]))
print("le nombre des canaux presents dans l'image et: {}".format(image.shape[2]))

# Chargement de l'image dans une fenêtre d'affichage cv2 window
cv2.imshow("image chargee", image)
#délais d'attente de press touche
cv2.waitKey(0) 
#enregistrement de l'image dans une autre format/fichier 
cv2.imwrite("Nouv_image.jpg", image)
