import numpy as np
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import kuegelifarbe
import time
import servoControl as sc

def removeDuplicateRows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))

append = True
NumberOfUniqueEntriesPerColor = 200
farben = ["rot", "gelb", "orange", "gruen"]
kf = kuegelifarbe.KuegeliFarbe()
data_targets = np.zeros((1,5),np.int32) 
#target = []
for index,farbe in enumerate(farben):
    entries = 0
    if farbe == "weiss":
        input("bitte weisses Papier vor Sensor halten und enter druecken")
    else:
        sc.zu(0)
        time.sleep(0.6)
        sc.auf(0)
        time.sleep(2)
        sc.zu(0)
        input("bitte Kugel mit Farbe {0} vor Sensor halten und enter druecken".format(farbe))
    #startVal = 0.9
    #endVal = 0.7
    #servoRange = np.arange(startVal, endVal, (endVal-startVal)/NumberOfUniqueEntriesPerColor)
    while entries<NumberOfUniqueEntriesPerColor-1:
        #sc.set_servo_pulse(0, servoRange[entries])
        rgba = kf.rgba()
        threshold = 150000000
        if rgba[0] == -1 or rgba == None or rgba[3]>threshold:
            continue
        #print ("rgb ",rgb, index)
        data_target = list(rgba)
        data_target.append(index) ## the index is the target
        #print (data_target)
        #print (data_targets)
        print (data_target)
        data_targets = np.append(data_targets,np.array(data_target).reshape(1,5),axis=0)
        
        #data_targets = removeDuplicateRows(data_targets)
        #print (data_targets)
         #print (len(data_targets))
        entries = len(data_targets) % (NumberOfUniqueEntriesPerColor)
        
        print( entries, index)
        time.sleep(0.05)


if append:
    with  open("data_target.txt","ab") as f:
        np.savetxt(f, data_targets)
else:
    np.savetxt("data_target.txt", data_targets)
    
data_targets = np.loadtxt("data_target.txt")
data = data_targets[:,:4]
target = data_targets[:,4]
from sklearn.externals import joblib
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size=0.1,random_state=0)

#clf = QuadraticDiscriminantAnalysis().fit(X_train,y_train)
clf = KNeighborsClassifier(5).fit(X_train,y_train)
print (clf.score(X_test,y_test))
joblib.dump(clf, 'rgbClassifier2.pkl')
print ("Fertig")
