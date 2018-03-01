
#**********************************
# visualising the data first
#


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('trainingdata.txt')

df2 = df[df.chageT < 4.0]
df3 = df[df.chageT > 4.0]

a = df2.as_matrix()
b = df3.as_matrix()



X = (a[:,0]).reshape(46,1)
y = (a[:,1]).reshape(46,1)

from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVC

lr = LinearRegression()
lr.fit(X,y)

print(lr.coef_)
print( lr.intercept_)

xi = np.arange(12)
yi = xi*lr.coef_ +lr.intercept_

plt.plot(a[:,0],a[:,1],'ro',xi,yi[0,:])
plt.show()

lr2 = LinearRegression()

X = (b[:,0]).reshape(54,1)
y = (b[:,1]).reshape(54,1)

lr.fit(X,y)

print (lr.coef_)
print (lr.intercept_)

xi = np.arange(12)
yi = xi*lr.coef_ +lr.intercept_

plt.plot(b[:,0],b[:,1],'ro',xi,yi[0,:])
plt.show()
