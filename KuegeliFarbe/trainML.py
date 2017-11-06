import numpy as np
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
def removeDuplicateRows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))

classes = ['red','yellow','green','orange']

for index,classs in enumerate(classes):
    print (index,classs)
    if index == 0:
        data = removeDuplicateRows(np.loadtxt(classs))
        target = np.zeros(len(data))
    else:
        clsdata =  removeDuplicateRows(np.loadtxt(classs))
        data = np.append(data,clsdata,axis=0)
        target=np.append(target,np.zeros(len(clsdata))+index)
            
print (len(data), len(target))
    #print (data)\n"

X_train,X_test,y_train,y_test = train_test_split(data,target,test_size=0.4,random_state=0)    
clf = QuadraticDiscriminantAnalysis().fit(X_train,y_train)
print (clf.score(X_test,y_test))
joblib.dump(clf, 'rgbClassifier.pkl') 
