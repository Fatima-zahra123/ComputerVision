import argparse
import cv2
"""
# dispatcher les arguments dans la table des arguments "dictionnaire" args
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter le chemin vers l'image")
args = vars(ap.parse_args())

#chargement du fichier dans un tableau nymPy
image = cv2.imread(args["image"])
"""
nomImage=input("donner le nom de l'image : \n")
image = cv2.imread(nomImage)
# # extraire  est afficher les informations couleurs de pixels [0,0]
# (b,g,r) = image[0,0]
# print("Pixel  (0,0) - Rouge: {}, Vert: {}, Bleu: {}".format(r,g,b))
# # changer la couleur du pixel 0,0 en rouge et re-aficher
# image[0,0] = (0,0,255)
# (b,g,r) = image[0,0]
# print("Pixel  (0,0) - Rouge: {}, Vert: {}, Bleu: {}".format(r,g,b))
# # Crouper une région de l'image et afficher 
# coin = image[0:100, 0:100]
# cv2.imshow("le coin de l'image", coin)
# cv2.waitKey(0)
# cv2.imwrite("coin.jpg",coin)
# # changer la couleur d'une zone entiere (en vert)
# image[0:100, 0:100] = (0,255,0)
# cv2.imshow("changement de couleur de la zone", image)
# cv2.waitKey(0)
imagenvdegris = image.copy()
imgGray = cv2.cvtColor(imagenvdegris,cv2.COLOR_BGR2GRAY)
cv2.imshow("changement de couleur de la zone", image)
cv2.imshow("changement de couleur de la zone", imgGray)

cv2.waitKey(0)





