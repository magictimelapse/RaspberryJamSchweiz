import numpy as np
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import kuegelifarbe
import time


def removeDuplicateRows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))


NumberOfUniqueEntriesPerColor = 400
farben = ["rot", "gelb", "orange", "gruen"]
kf = kuegelifarbe.KuegeliFarbe()
data_targets = np.zeros((1,5),np.int32) 
#target = []
for index,farbe in enumerate(farben):
    entries = 0
    if farbe == "weiss":
        input("bitte weisses Papier vor Sensor halten und enter druecken")
    else:
        input("bitte Kugel mit Farbe {0} vor Sensor halten und enter druecken".format(farbe))
    while entries<NumberOfUniqueEntriesPerColor-1:
        rgba = kf.rgba()
        threshold = 40
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
        time.sleep(0.1)



np.savetxt("data_target.txt", data_targets)
data = data_targets[:,:4]
target = data_targets[:,4]
from sklearn.externals import joblib
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size=0.1,random_state=0)

clf = QuadraticDiscriminantAnalysis().fit(X_train,y_train)
print (clf.score(X_test,y_test))
joblib.dump(clf, 'rgbClassifier2.pkl')
print ("Fertig")
