import io
import time
import picamera
import cv2
import numpy as np
import os
path = '/home/pi/opencv/data/haarcascades/'
face_cascade = cv2.CascadeClassifier(os.path.join(path,'haarcascade_frontalface\
_default.xml'))
eye_cascade = cv2.CascadeClassifier(os.path.join(path,'haarcascade_eye.xml'))

# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    ii =0
    f=0
    while True:
        camera.capture(stream, format='jpeg',resize=(320,240))
        
        # Construct a numpy array from the stream
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        # "Decode" the image from the array, preserving colour
        image = cv2.imdecode(data, 1)
        # OpenCV returns an array with data in BGR order. If you want RGB instead
        # use the following...
        img = image.copy()#image[:, :, ::-1].copy()
        #img =  img.transpose((1, 2, 0)).astype(np.uint8).copy() 
        print ii
        ii +=1
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        print ii
        for (x,y,w,h) in faces:
            print "face detected at ", x,y
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                f+=1
            cv2.imwrite('images/face_{0:05d}.jpg'.format(f),img)
        stream.seek(0)
        stream.truncate()
