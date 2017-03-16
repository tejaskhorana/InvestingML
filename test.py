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
print '\nImages (image of the digit basically converted to numbers)'
print (digits.images[0])

#classifier
clf = svm.SVC(gamma=0.001, C=100)

#store data and target answer EXCEPT FOR the last index
#this is our training data
x,y = digits.data[:-1], digits.target[:-1]

#fit the SVM model according to the given training data.
clf.fit(x,y)

#last element!
print('Prediction: ', clf.predict(digits.data[-1]))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()