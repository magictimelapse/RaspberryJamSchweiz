import io
import time
from picamera import PiCamera
import cv2
import numpy as np
# wir wollen die mit der Kamera aufgenommenen Bilder auf einen Bilderstrom (stream auf englisch) schreiben:
stream = io.BytesIO()
#wir oeffnen die Kamera:
camera = PiCamera()
# wir brauchen einen Zaehler, damit wir die Bilder in aufsteigender Reihenfolge speichern koennen
Zaehler = 0
#und starten dann den Loop, welcher fuer immer laeuft:
while True:
    #mit diesem Befehl nehmen wir ein Bild auf, und verkleinern es auf 320x240 Pixeln, damit wir es spaeter leichter bearbeiten koennen.
    camera.capture(stream,format='jpeg', resize=(320,240))
    # jetzt muessen wir die aufgenommenen Daten etwas herumbeigen, damit wir es spaeter mit opencv bearbeiten koennen:
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    img = cv2.imdecode(data,1).copy()
    # img ist ein Bild im opencv Format. Wir koennen dieses jetzt auf die Festplatte speichern:
    cv2.imwrite('Bilder/Bilder_{0:05d}.jpg'.format(Zaehler),img)
    Zaehler = Zaehler + 1
    # damit das naechste Bild geladen wird, muessen wir noch den stream zurueckspulen:
    stream.seek(0)
    stream.truncate()

    
