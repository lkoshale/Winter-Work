
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

mglearn.plots.plot_linear_regression_wave()
#plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X,y = mglearn.datasets.load_extended_boston()

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)

lr = LinearRegression().fit(X_train,y_train)


print("Linear Reg weights:%s"%lr.coef_)
print("Linear Reg intercept:%s"%lr.intercept_)

print("test acuracy: %0.2f"%lr.score(X_test,y_test))
print("train acuracy: %0.2f"%lr.score(X_train,y_train))


print "-***********************-"

#with regularization
from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0).fit(X_train,y_train)

print("Ridge (with regularization)test acuracy: %0.2f"%ridge.score(X_test,y_test))
print("ridge train acuracy: %0.2f"%ridge.score(X_train,y_train))

ridge10 = Ridge(alpha=10).fit(X_train, y_train)
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)

plt.plot(ridge.coef_, 's', label="Ridge alpha=1")
plt.plot(ridge10.coef_, '^', label="Ridge alpha=10")
plt.plot(ridge01.coef_, 'v', label="Ridge alpha=0.1")
plt.plot(lr.coef_, 'o', label="LinearRegression")
plt.xlabel("Coefficient index")
plt.ylabel("Coefficient magnitude")
plt.hlines(0, 0, len(lr.coef_))
plt.ylim(-25, 25)
plt.legend()
plt.show()

#mglearn.plots.plot_ridge_n_samples()

plt.show()

print "***********************************"

# with regul but some coeff close to zero
from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.01,max_iter=100000).fit(X_train,y_train)

print("Lasso test acuracy: %0.2f"%lasso.score(X_test,y_test))
print("Lasso train acuracy: %0.2f"%lasso.score(X_train,y_train))
print("Number of feature used : %d"%np.sum(lasso.coef_!=0))

