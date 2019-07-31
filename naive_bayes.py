from preprocess import preprocess as p
from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
f_train, f_test, l_train, l_test = p.vectorize()
classifier.fit(f_train, l_train)

print("accuracy: " + str(classifier.score(f_test, l_test)))