import numpy as np
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
data_targets = np.loadtxt("data_target.txt")

##remove colors ##
new_data_targets = np.zeros((1,4),np.float32) 
for data_target in data_targets:
    if data_target[3] != 0 and  data_target[3] != 1 and  data_target[3] != 2:
        new_data_targets = np.append(new_data_targets, data_target.reshape(1,4),axis=0)
new_data_targets = np.delete(new_data_targets,(0), axis=0)
print (new_data_targets)
data = new_data_targets[:,:3]
target = new_data_targets[:,3]
#data = StandardScaler().fit_transform(data)
#print (data)
#print (target)
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size=0.3,random_state=0)
classifiers =[
     KNeighborsClassifier(3),
     KNeighborsClassifier(5),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    #GaussianProcessClassifier(1.0 * RBF(1.0)),
    #DecisionTreeClassifier(max_depth=5),
    # RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    #MLPClassifier(alpha=1),
    #AdaBoostClassifier(),
    #GaussianNB(),
    #QuadraticDiscriminantAnalysis()
]
maxScore = 0
for classifier in classifiers:
    clf = classifier.fit(X_train,y_train)
    score = clf.score(X_test,y_test)
    print (score)
    if score> maxScore:
        maxScore = score
        joblib.dump(clf, 'rgbClassifier2.pkl') 
