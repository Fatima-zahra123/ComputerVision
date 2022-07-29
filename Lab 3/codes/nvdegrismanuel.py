import cv2
image = cv2.imread('./fleurs.jpg')
imagenvdegris = image.copy()
#get image dimensions 
h=image.shape[0]
w=image.shape[1]

#loop over the image

for y in range (0,h):
    for x in range (0,w):
        (b,g,r) = imagenvdegris[y,x]
        imagenvdegris[y,x]=b/30

cv2.imshow('Original image',image)
cv2.imshow('Gray Image',imagenvdegris)

for y in range (0,h):
    for x in range (0,w):
        (b,g,r) = imagenvdegris[y,x]
        imagenvdegris[y,x]=b*30

cv2.imshow('Gray Image 2',imagenvdegris)
cv2.waitKey(0)
cv2.destroyAllWindows()