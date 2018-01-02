
#important imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
print iris_dataset.viewkeys()

# shuflle the data and then partion in test and train set
X_train,X_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)

print("train size %s and test size %s" %(y_train.shape,y_test.shape ))

iris_dataframe = pd.DataFrame(X_train,columns=iris_dataset.feature_names)

# create a scatter matrix from the dataframe, color by y_train

grr = pd.plotting.scatter_matrix(iris_dataframe,c=y_train,figsize=(15,15),marker='o',hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
#plt.show()

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)

X_new = np.array([[5, 2.9, 1, 0.2]])

predict = knn.predict(X_new)
print iris_dataset['target_names'][predict]

y_pred = knn.predict(X_test)
print("values predicted : %s"%y_pred)
print("actual values %s:"%y_test)

accuracy = np.mean( y_pred==y_test)
print("acuuracy is : %s" %accuracy)

print knn.score(X_test,y_test)