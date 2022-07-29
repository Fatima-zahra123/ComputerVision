import argparse
import cv2

# Récupération du tableau des arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Entrez le chemin de l'image")
ap.add_argument("-x", "--px", required = True, help = "Entrez le x du pixel")
ap.add_argument("-y", "--py", required = True, help = "Entrez le y du pixel")

args = vars(ap.parse_args())

# Chargement et convertion de l'image en tableau numpy array
# Affichage des caractérisrtiques 
image = cv2.imread(args["image"])
# recuppérer la position de découpage à partir des arguments
px=int(args["px"])
py=int(args["py"])
if (px>image.shape[0])or(py>image.shape[1]):
	print("pixels hors taille image\n")
else:
	#extraction du tuple (informations couleurs) qui se trouve à la position px et py 
	(b,v,r)=image[int(px),int(py)]
	print("le pixel en {} {}- rouge: {}, vert: {},bleu  {}".format(px,py,r,v,b))
	# extraction d'une sub- zone  200 x 200 à partir de l'image original
	if (px+200>image.shape[0])or(py+200>image.shape[1]):
		print("Le recadrement n'est pas possible\n")
	else:
		zone=image[int(px):int(px)+200,int(py):int(py)+200]
		#afficher cette zone
		cv2.imshow("Zone",zone)
		# délais d'attente 10s
		cv2.waitKey(10000)
		# enregistrer la zone dans une nouvelle image  
		cv2.imwrite("Zone{}x{}.jpg".format(px,py),zone)
