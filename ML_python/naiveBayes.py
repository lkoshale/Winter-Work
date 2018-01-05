import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

cancer = load_breast_cancer()
X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,stratify=cancer.target,random_state=42)

gb = GaussianNB().fit(X_train,y_train)
lg = LogisticRegression(C=100).fit(X_train,y_train)

print( "Gausian in test set acuracy : %0.4f"%(gb.score(X_test,y_test)))
print( "Logistic in test set acuracy : %0.4f"%(lg.score(X_test,y_test)))