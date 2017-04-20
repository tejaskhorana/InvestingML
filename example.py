import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

#print(digits.data)
#print(digits.target)
#print(digits.images[0])

#setup classifier
#Gamma: how quickly get to base of mountain using gradient descent? High: Bigger jumps, super fast, get stuck at local minima. Hard to center in on absolute base. Tiny jumps: takes a long time but better chance of hitting the correct answer
classifier = svm.SVC(gamma=0.001, C=100)
#load up one less than amount than data to use as training set
x, y = digits.data[:-10], digits.target[:-10]
#fits a line to the numbers maximizing margins
classifier.fit(x,y)

#predicts last element
print('Prediction: ', classifier.predict(digits.data[-3]))
plt.imshow(digits.images[-3], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()