import cv2
import time
import numpy as np
haar_cascade = 'haarcascades/haarcascade_car.xml'
video='clear_road.mp4'
      
cap = cv2.VideoCapture(video)
car_cascade = cv2.CascadeClassifier(haar_cascade)

# reads frames from a video
ret, frames = cap.read()
        
# convert frames to gray scale 
gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        
# Detects cars of different sizes in the input image
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

# To draw a rectangle in each cars
for (x,y,w,h) in cars:
  if y>0 and w>70:
    cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(frames,str(int(4000/(y+h)))+'m', (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    
# Display frames in a window 
cv2.imshow('video', frames)

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    frames= cv2.resize(frames, (1280,720), interpolation = cv2.INTER_AREA)
        
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray,(5,5),0)
    #dilated = cv2.dilate(blur,np.ones((3,3)))
    #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    #closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel) 
    
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
      if y>0 and w>70:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,255,255),3)
        cv2.rectangle(frames, (x, y), (x+w , y-40), (0,100,100), -1)
        cv2.putText(frames,str(int(4000/(y+h)))+'m', (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    
    # Display frames in a window 
    cv2.imshow('video', frames)        
    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
    
# De-allocate any associated memory usage
cv2.destroyAllWindows()
