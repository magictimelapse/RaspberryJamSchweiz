
import cv2
import numpy as np
import os
import io
import time
from picamera import PiCamera

Pfad = '/home/pi/opencv/data/haarcascades/'
GesichtsKaskade = cv2.CascadeClassifier(os.path.join(Pfad,'haarcascade_frontalface_default.xml'))
AugenKaskade = cv2.CascadeClassifier(os.path.join(Pfad,'haarcascade_eye.xml'))
# Funktion zur Gesichtserkennung:
def Gesichtserkennung(img,GesichtsKaskade, AugenKaskade):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gesichter = GesichtsKaskade.detectMultiScale(gray, 1.3, 5)
    for x,y,w,h in gesichter:
        print "Gesicht gefunden an Position ", x,y, "!"
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        augen = AugenKaskade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in augen:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return img



stream = io.BytesIO()
camera = PiCamera()
Zaehler = 0
while True:
    camera.capture(stream,format='jpeg', resize=(320,240))
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    img = cv2.imdecode(data,1).copy()

    ## jetzt fuehren wir die Gesichtserkennung durch:
    imgGesichter = Gesichtserkennung(img,GesichtsKaskade,AugenKaskade)
    # und speichern das Bild mit den gefundenen Gesichtern ab:
    cv2.imwrite('Bilder/BilderGesicht_{0:05d}.jpg'.format(Zaehler),img)
    Zaehler = Zaehler+1
    stream.seek(0)
    stream.truncate()

