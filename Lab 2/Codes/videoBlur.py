import cv2


# to detect the face of the human 

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

cap = cv2.VideoCapture(r"C:\Users\pc\Pictures\Camera\20210708_213427.mp4")
cap = cv2.VideoCapture(0)
# cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)

# cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
while(True):

# Capture frame-by-frame

    ret, frame = cap.read()

# Display the resulting frame

    
# convert the frame into grayscale(shades of black & white) 

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    face = cascade.detectMultiScale(gray_image, 

                                scaleFactor=2.0, 

                                minNeighbors=4)
    print(face)

    for x, y, w, h in face: 

    # draw a border around the detected face. 

    # (here border color = green, and thickness = 3) 

        image = cv2.rectangle(frame, (x, y), 

                          (x+w, y+h),  

                          (0, 255, 0), 3) 
        
        image[y:y+h, x:x+w] = cv2.medianBlur(image[y:y+h, x:x+w], 

                                             35) 

    cv2.imshow("preview",frame)

#Waits for a user input to quit the application

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()