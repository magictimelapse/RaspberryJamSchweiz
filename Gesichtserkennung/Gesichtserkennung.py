import cv2
import numpy as np
import os
#
# an diesem Pfad befinden sich die Dateien fuer die Gesichtserkennung
Pfad = '/home/pi/opencv/data/haarcascades/'
# mit diesem File koennen Gesichter erkannt werden:
GesichtsKaskade = cv2.CascadeClassifier(os.path.join(Pfad,'haarcascade_frontalface\
_default.xml'))
# mit diesem File werden Augen identifiziert:
AugenKaskade = cv2.CascadeClassifier(os.path.join(Pfad,'haarcascade_eye.xml'))

## wir definieren eine Funktion, in welcher Gesichter und Augen erkannt werden, und ein Rahmen um das Gesicht und die Augen auf das Bild gemalt werden:
def Gesichtserkennung(img,GesichtsKaskade,AugenKaskade):
    # zuerst muessen wir das farbige Bild in Graustufen verwandeln:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # dann benuetzen wir die cv2 Bibliothek, um Gesichter zu erkennen:
    gesichter = GesichtsKaskade.detectMultiScale(gray, 1.3, 5)
    # in "gesichter" sind die Koordinaten der gefundenen Gesichter gespeichert. Wir machen eine Schlaufe ueber alle Gesichter im Bild:
    for x,y,w,h in gesichter:
        print "Gesicht gefunden an Position ", x,y, "!"
        # wir zeichnen einen blauen Rahmen um das Gesicht:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        # im Gesicht suchen wir nach Augen. Dazu schneiden wir das Gesicht aus dem Bild heraus:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        # dann erkennen wir genau gleich wie oben das Gesicht die Augen:
        augen = AugenKaskade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in augen:
            # und zeichnen auf das urspruengliche Bild einen gruenen Rahmen:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # das Bild mit den Rahmen um die Gesichter und Augen geben wir zurueck:
    return img

