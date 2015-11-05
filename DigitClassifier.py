from sklearn import svm
from sklearn import datasets
'''
->importing SVM and datasets from sklearn
->classify digits using support vector classification
->manually chose gamma, but could have used grid search
->train data using clf.fit(data,target) method
'''
#load
iris = datasets.load_iris()
digits = datasets.load_digits()
#print(digits.data)
#classify
clf = svm.SVC(gamma=0.001, C=100.) #classifier using support vector classification
#train
clf.fit(digits.data[:-1],digits.target[:-1])
'''
OUT:

SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
  gamma=0.001, kernel='rbf', max_iter=-1, probability=False,
  random_state=None, shrinking=True, tol=0.001, verbose=False)
**Can store using:
>>> from sklearn.externals import joblib
>>> joblib.dump(clf, 'filename.pkl')
**then later retrive that file:
>>> clf = joblib.load('filename.pkl') 
'''
#now classify some digs
clf.predict(digits.data[-1])
#last image looks like an 8!
