# import the necessary packages
from PIL import Image
import pytesseract
#import argparse
import cv2
import os

# construire le parseur d'argument pour 2 argument 
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="le chemin de l'image à traiter ")
ap.add_argument("-p", "--pretraitement", type=str, default="seuil",
	help="type de pré-traitement sur l'image à effectuer avant de scanné le contenus")
args = vars(ap.parse_args())
"""
# charger l'image et la convertir en niveau de gris
image = cv2.imread("test.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)
cv2.waitKey(4000)
pretraitemen = "seuil"
# Verifier si un seuillage doit être aappliqué a l'image
if pretraitement == "seuil":
	gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Verfifer si un flou median doit être appliqué pour supprimer le bruit
elif pretraitement == "bruit":
	gray = cv2.medianBlur(gray, 3)

# enregistrer l'image en niveau de gris sur le disque comme fichier temporel 
# pour lui appliquer l'OCR (avec génération de non à partir du PID du processus actuel
nom_fichier = "temp{}.png".format(os.getpid())
cv2.imwrite(nom_fichier, gray)
# charger l'image comme image PIL/Pillow, appliquer le système de reconnaissance, 
# ensuite supprimer l'image temporelle du disque
# et enfin afficher le texte detecter
text = pytesseract.image_to_string(Image.open(nom_fichier))
os.remove(nom_fichier)
print(text)

# afficher les image de sortie
# cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)

# Utilisation
# python3 code_lab.py --image ../materiels/example_01.png 
# python3 code_lab.py --image ../materiels/example_02.png  --pretraitement bruit
