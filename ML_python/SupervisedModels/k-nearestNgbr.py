
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

mglearn.plots.plot_knn_classification(n_neighbors=3)
#plt.show()

from sklearn.model_selection import train_test_split

X,y = mglearn.datasets.make_forge()

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)

clf.fit(X_train,y_train)

print("clf score : %0.2f"%clf.score(X_test,y_test))


fig, axes = plt.subplots(1, 3, figsize=(10, 3))
#
# for n_neighbors, ax in zip([1, 3, 9], axes):
#     # the fit method returns the object self, so we can instantiate
#     # and fit in one line
#     clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
#     mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
#     mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
#     ax.set_title("{} neighbor(s)".format(n_neighbors))
#     ax.set_xlabel("feature 0")
#     ax.set_ylabel("feature 1")
# axes[0].legend(loc=3)

#plt.show()


from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
#print cancer.target

X_train,X_test,y_train,y_test = train_test_split(cancer['data'],cancer['target'],stratify=cancer.target,random_state=0)

training_acuracy = []
test_acuracy = []
neighbours_setting = range(1,11)

for n in neighbours_setting:
    clf = KNeighborsClassifier(n_neighbors=n)
    clf.fit(X_train,y_train)
    training_acuracy.append(clf.score(X_train,y_train))
    test_acuracy.append(clf.score(X_test,y_test))


plt.plot(neighbours_setting,training_acuracy, label="training accuracy")
plt.plot(neighbours_setting,test_acuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()

mglearn.plots.plot_knn_regression(n_neighbors=3)

from sklearn.neighbors import KNeighborsRegressor

X,y = mglearn.datasets.make_wave(n_samples=40)

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)

reg = KNeighborsRegressor(n_neighbors=3)
reg.fit(X_train,y_train)

print("regression score %0.2f"%reg.score(X_test,y_test))


fig, axes = plt.subplots(1, 3, figsize=(15, 4))
# create 1,000 data points, evenly spaced between -3 and 3
line = np.linspace(-3, 3, 1000).reshape(-1, 1)

for n_neighbors, ax in zip([1, 3, 9], axes):
    # make predictions using 1, 3, or 9 neighbors
    reg = KNeighborsRegressor(n_neighbors=n_neighbors)
    reg.fit(X_train, y_train)
    ax.plot(line, reg.predict(line))
    ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
    ax.plot(X_test, y_test, 'v', c=mglearn.cm2(1), markersize=8)

    ax.set_title(
    "{} neighbor(s)\n train score: {:.2f} test score: {:.2f}".format(
    n_neighbors, reg.score(X_train, y_train),
    reg.score(X_test, y_test)))

    ax.set_xlabel("Feature")
    ax.set_ylabel("Target")

axes[0].legend(["Model predictions", "Training data/target","Test data/target"], loc="best")

plt.show()