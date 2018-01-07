# Neural networks also
# expect all input features to vary in a similar way,
#  and ideally to have a mean of 0, and a variance of 1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split


X, y = make_moons(n_samples=100, noise=0.25, random_state=3)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,random_state=42)

# single hidden layer with 10 units , algo l-bfgs and function is relu

mlp = MLPClassifier(solver='lbfgs', random_state=0,hidden_layer_sizes=[10]).fit(X_train, y_train)

mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")

# plt.show()

## multi layer

# using two hidden layers, with 10 units each

mlp = MLPClassifier(solver='lbfgs', random_state=0,hidden_layer_sizes=[10, 10])
mlp.fit(X_train, y_train)

mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)

plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
# plt.show()

## with tanh non linearity

# using two hidden layers, with 10 units each, now with tanh nonlinearity
mlp = MLPClassifier( solver='lbfgs', activation='tanh',random_state=0, hidden_layer_sizes=[10, 10])
mlp.fit(X_train, y_train)

mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
# plt.show()

# also has alpha same as linear regressor (lambda)


# fig, axes = plt.subplots(2, 4, figsize=(20, 8))
# for axx, n_hidden_nodes in zip(axes, [10, 100]):
#     for ax, alpha in zip(axx, [0.0001, 0.01, 0.1, 1]):
#         mlp = MLPClassifier(solver='lbfgs', random_state=0,
#                             hidden_layer_sizes=[n_hidden_nodes, n_hidden_nodes],alpha=alpha)
#         mlp.fit(X_train, y_train)
#         mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3, ax=ax)
#         mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train, ax=ax)
#         ax.set_title("n_hidden=[{}, {}]\nalpha={:.4f}".format(n_hidden_nodes, n_hidden_nodes, alpha))
#
# plt.show()



## with difrrent seed value as initail weights are randomized

# fig, axes = plt.subplots(2, 4, figsize=(20, 8))
#
# for i, ax in enumerate(axes.ravel()):
#     mlp = MLPClassifier(solver='lbfgs', random_state=i,hidden_layer_sizes=[100, 100])
#     mlp.fit(X_train, y_train)
#     mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3, ax=ax)
#     mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train, ax=ax)
#
# plt.show()


## on real data and feature scaling

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

mlp = MLPClassifier(random_state=42)
mlp.fit(X_train, y_train)

print("Accuracy on training set: {:.2f}".format(mlp.score(X_train, y_train)))
print("Accuracy on test set: {:.2f}".format(mlp.score(X_test, y_test)))


# compute the mean value per feature on the training set
mean_on_train = X_train.mean(axis=0)
# compute the standard deviation of each feature on the training set
std_on_train = X_train.std(axis=0)
# subtract the mean, and scale by inverse standard deviation
# afterward, mean=0 and std=1
X_train_scaled = (X_train - mean_on_train) / std_on_train
# use THE SAME transformation (using training mean and std) on the test set
X_test_scaled = (X_test - mean_on_train) / std_on_train

mlp = MLPClassifier(max_iter=1000,random_state=0)
mlp.fit(X_train_scaled, y_train)

print("Accuracy on training set: {:.3f}".format(mlp.score(X_train_scaled, y_train)))
print("Accuracy on test set: {:.3f}".format(mlp.score(X_test_scaled, y_test)))


mlp = MLPClassifier(max_iter=1000, alpha=1, random_state=0)
mlp.fit(X_train_scaled, y_train)
print("Accuracy on training set: {:.3f}".format(
mlp.score(X_train_scaled, y_train)))
print("Accuracy on test set: {:.3f}".format(mlp.score(X_test_scaled, y_test)))