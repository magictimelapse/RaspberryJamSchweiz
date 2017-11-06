import kuegelifarbe
import time
import numpy as np
from sklearn.preprocessing import StandardScaler
kf = kuegelifarbe.KuegeliFarbe()
from sklearn.externals import joblib
clf = joblib.load("rgbClassifier2.pkl")
farben = ["weiss", "rot", "gelb", "orange", "gruen"]
while True:
    farbe = np.array(kf.rgb()).reshape(1,-1)
    rgb = kf.rgb()
    if rgb[0] == -1 or rgb == None or rgb[0]==255 or rgb[1] == 255 or rgb[2] == 255:
        continue
    #farbe = StandardScaler().fit_transform(farbe)
    #print (farbe)
    farbe =  np.array(rgb).reshape(1,-1)
    print (farbe)
    a = clf.predict(farbe)[0]
    print (a)
    print (farben[int(a)])
    #    print (farbe)
    time.sleep(0.25)
