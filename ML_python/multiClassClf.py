
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

Gshow = False
 # Gshow = True

from sklearn.datasets import make_blobs
from sklearn.svm import LinearSVC

X,y = make_blobs(random_state=42)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.legend(["Class 0", "Class 1", "Class 2"])

if Gshow :
    plt.show()

linear_svm = LinearSVC().fit(X,y)