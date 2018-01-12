
import pandas as pd
import numpy as np
import seaborn as sbs
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

rawData = pd.read_csv('criminal_train.csv')

X_raw = rawData.as_matrix()
y_raw = X_raw[:,71]
X_raw = X_raw[:,1:70]

X_train,X_test,y_train,y_test = train_test_split(X_raw,y_raw,random_state=0)

y_raw = y_raw[:]
X_raw = X_raw[:,1:9]

from sklearn.decomposition import PCA
import mglearn

pca = PCA(n_components=2)
pca.fit(X_raw)
X_pca = pca.transform(X_raw)

fp = pd.DataFrame(X_pca)

pd.plotting.scatter_matrix(fp,c=y_raw,figsize=(15,15),marker='o')
plt.show()

print(pca.components_)

# from sklearn.neighbors import KNeighborsClassifier
#
# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(X_train,y_train)
# print(" test acrcy : %0.4f"%(knn.score(X_test,y_test)))
# print(" train acrcy : %0.4f"%(knn.score(X_train,y_train)))
# print np.sum(knn.predict(X_test))
# print X_test.shape
#
# ## its predicting all 0
# from sklearn.linear_model import LogisticRegression
#
# lg = LogisticRegression(C=100)
# lg.fit(X_train,y_train)
# print(" test acrcy : %0.4f"%(lg.score(X_test,y_test)))
# print(" train acrcy : %0.4f"%(lg.score(X_train,y_train)))
# print np.sum(lg.predict(X_test[:,:]))

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train,y_train)
print(" test acrcy : %0.4f"%(clf.score(X_test,y_test)))
print(" train acrcy : %0.4f"%(clf.score(X_train,y_train)))
print np.sum(clf.predict(X_test[:,:]))


def plot_feature_importances_cancer(model):
    n_features = rawData.columns.values[1:70].size
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), rawData.columns.values[1:70])
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")


plt.rcParams['ytick.labelsize'] = 4
# plot_feature_importances_cancer(clf)
# plt.show()

tDF = rawData[ ['IFATHER','GRPHLTIN','IIMEDICR','IRPINC3','IRFAMIN3','VESTR','VEREP'] ]

# pd.plotting.scatter_matrix(tDF,c=y_raw,figsize=(15,15),marker='o')
# plt.show()

pca2 = PCA(n_components=2)
pca2.fit(tDF)
pd.plotting.scatter_matrix(pd.DataFrame(pca2.transform(tDF)),c=y_raw,figsize=(15,15),marker='o')
plt.show()

# from sklearn.manifold import TSNE
#
# tsne = TSNE(random_state=42)
# pd.plotting.scatter_matrix(pd.DataFrame(tsne.fit_transform(tDF)),c=y_raw,figsize=(15,15),marker='o')
# plt.show()


imputaionIndicator = ['IIHHSIZ2','IIKI17_2','IIHH65_2','IIMCDCHP','IIMEDICR','IICHMPUS','IIPRVHLT','IIOTHHLT'
                      ,'IIINSUR4','IIFAMSOC','IIFAMSSI','IIFSTAMP','IIFAMPMT','IIFAMSVC','IIWELMOS'
                      ,'IIFAMIN3']

medical = ['MEDICARE','CAIDCHIP','CHAMPUS','PRVHLTIN','GRPHLTIN'	,'HLTINNOS'	,'HLCNOTYR'	,'HLCNOTMO'	,
           'HLCLAST','HLLOSRSN'	,'HLNVCOST'	,'HLNVOFFR'	,'HLNVREF'	,'HLNVNEED'	,'HLNVSOR'	,'IRMCDCHP'	,
           'IIMCDCHP'	,'IRMEDICR'	,'IIMEDICR'	,'IRCHMPUS','IICHMPUS'	,'IRPRVHLT'	,'IIPRVHLT'	,'IROTHHLT'	,
           'IIOTHHLT'	,'HLCALLFG'	,'HLCALL99'	,'ANYHLTI2'	,'IRINSUR4'	,'IIINSUR4','OTHINS' ]

# remove the imputation colmns
medicalRevised = [item for item in medical if item not in imputaionIndicator]



