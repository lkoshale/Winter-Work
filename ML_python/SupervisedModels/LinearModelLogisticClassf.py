import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

# st = str(raw_input())
# if (st=="Y" or st == "y"):
#
# else:

Gshow = False
Gshow = True

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

X,y = mglearn.datasets.make_forge()

fig, axes = plt.subplots(1, 2, figsize=(10, 3))


for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
    clf = model.fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5,
    ax=ax, alpha=.7)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title("{}".format(clf.__class__.__name__))
    ax.set_xlabel("Feature 0")
    ax.set_ylabel("Feature 1")

axes[0].legend()
if Gshow :
    plt.show()



#show effect of C
mglearn.plots.plot_linear_svc_regularization()
if Gshow :
    plt.show()


# another databse

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer();
X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,stratify=cancer.target,random_state=42)

logreg = LogisticRegression().fit(X_train,y_train)

logreg001 = LogisticRegression(C=0.01).fit(X_train,y_train)
logreg100 = LogisticRegression(C=100).fit(X_train,y_train)

print("Logistic Reg train acc:%0.3f"%logreg.score(X_train,y_train))
print("Logistic Reg test acc:%0.3f"%logreg.score(X_test,y_test))


plt.plot(logreg.coef_.T, 'o', label="C=1")
plt.plot(logreg100.coef_.T, '^', label="C=100")
plt.plot(logreg001.coef_.T, 'v', label="C=0.001")
plt.xticks(range(cancer.data.shape[1]), cancer.feature_names, rotation=90)
plt.hlines(0, 0, cancer.data.shape[1])
plt.ylim(-5, 5)
plt.xlabel("Coefficient index")
plt.ylabel("Coefficient magnitude")
plt.legend()

if Gshow :
    plt.show()