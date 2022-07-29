import numpy as np
import cv2 as cv

img = cv.imread("coins.jpg")
img_gris=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Affichage1',img_gris)
img_gris=cv.medianBlur(img_gris,5)
cv.imshow('Affichage2',img_gris)
#planets.jpg  cercles=cv.HoughCircles(img_gris,cv.HOUGH_GRADIENT,1,150,param1=280,param2=29.5, minRadius=0,maxRadius=0)
cercles=cv.HoughCircles(img_gris,cv.HOUGH_GRADIENT,2,120,param1=200,param2=29.5, minRadius=0,maxRadius=0)

cercles=np.around(cercles)
print(cercles)
for (x,y,r)in cercles[0,:]:
    cv.circle(img,(x,y),r,(0,255,0),3)
    cv.circle(img,(x,y),1,(0,0,0),3)
cv.imshow('Affichage',img)

cv.waitKey()
cv.destroyAllWindows()