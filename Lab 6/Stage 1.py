import numpy as np
import cv2 as cv

img = cv.imread("smarties.jpg")
img_gris=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img_gris=cv.medianBlur(img_gris,5)
cercles=cv.HoughCircles(img_gris.cv.HOUGH_GRADIANT,1,200,param1=100,param2=29.5, minRadius=0,maxRadius=0)


cerclDetect=np.around(cercles)
for (x,y,r)in cerclDetect[0,:]:
    cv.circle(img,(x,y),r,(0,255,0),3)
    cv.circle(img,(x,y),1,(0,0,0),3)
cv.imshow('Affichage',img)
cv.waitKey()
cv.destroyAllWindows()