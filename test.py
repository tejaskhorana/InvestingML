# Author: Tejas Khorana
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

#Returns a dictionary-like object with data, images, target, target_names, DESCR
digits = datasets.load_digits()

#the data to learn
print '\nData'
print (digits.data)

#the classification labels for each sample
print '\nTarget'
print (digits.target)

#the images corresponding to each sample
print '\nImage #1 (image of the first digit basically converted to numbers)'
print (digits.images[0])

#classifier, 
clf = svm.SVC(gamma=0.001, C=100)

#store data and target answer EXCEPT FOR the last index
#this is our training data
x,y = digits.data[:-10], digits.target[:-10]

#fit the SVM model according to the given training data.
clf.fit(x,y)

#last element!
print 'Prediction: '
print clf.predict(digits.data[[-3]])[0] 
plt.imshow(digits.images[-3], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()

