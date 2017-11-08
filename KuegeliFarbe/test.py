import kuegelifarbe
import time
import numpy as np
from sklearn.preprocessing import StandardScaler
kf = kuegelifarbe.KuegeliFarbe()
from sklearn.externals import joblib
clf = joblib.load("rgbClassifier2.pkl")
farben = ["rot", "gelb", "orange", "gruen"]
while True:
    #farbe = np.array(kf.rgba()).reshape(1,-1)
    rgba = kf.rgba()
    threshold = 400
    if rgba[0] == -1 or rgba == None or rgba[3]>threshold:
        continue
    #farbe = StandardScaler().fit_transform(farbe)
    #print (farbe)
    farbe =  np.array(rgba).reshape(1,-1)
    print (farbe)
    a = clf.predict(farbe)[0]
    print (a)
    print (farben[int(a)])
    #    print (farbe)
    time.sleep(0.25)
