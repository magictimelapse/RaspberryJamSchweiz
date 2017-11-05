import kuegelifarbe
import time
kf = kuegelifarbe.KuegeliFarbe()

while True:
    farbe = kf.farbe()
    if farbe.find("weiss") <0:
        print (farbe)
        #time.sleep(0.5)
