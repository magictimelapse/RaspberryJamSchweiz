import kuegelifarbe
import numpy as np
kf = kuegelifarbe.KuegeliFarbe()
from sklearn.externals import joblib
clf = joblib.load("rgbClassifier2.pkl")
farben = ["rot", "gelb", "orange", "gruen","leer"]

def gibFarbe():
    rgba = kf.rgba()

    
    farbe =  np.array(rgba).reshape(1,-1)
    #print (farbe)
    a = clf.predict(farbe)[0]
    return farben[int(a)]
