import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,stratify=cancer.target,random_state=42)

gb = GaussianNB().fit(X_train,y_train)

print( "in test set acuracy : %0.2f"%(gb.score(X_test,y_test)))
