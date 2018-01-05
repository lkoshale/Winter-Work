import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df3 = pd.read_csv('train.csv')

# df3.info()
# print df3.head()

#parse the DATA

#dropping the data not required
df = df3.drop(['PassengerId','Name','Ticket','Cabin','SibSp', 'Parch'],axis=1)


# for now drop age also
# df = df2.drop(['Age'],axis=1)
# df["Age"].fillna(lambda x: random.choice(df[df['Age'] != np.nan]["Age"]), inplace =True)

#random select age
df['Age']=df['Age'].apply(lambda x: np.random.choice([x for x in range(int(min(df['Age'])),int(max(df['Age'])))]) if (np.isnan(x)) else x)

# fill missing values
df.Embarked.fillna('S',inplace=True)

# nothing lef
print df.isnull().sum()


# Sex and Embarked are string convert them into numreals

from sklearn.preprocessing import LabelEncoder


le1 = LabelEncoder()
le2 = LabelEncoder()

le1.fit(list(df['Sex'].values))
df['Sex'] = le1.transform(list(df['Sex'].values))

le2.fit(list(df['Embarked'].values))
df['Embarked'] = le2.transform(list(df['Embarked'].values))

# print df.info()
# print df.apply(pd.Series.nunique)


# pd.plotting.scatter_matrix(df,figsize=(15,15),marker='o',hist_kwds={'bins': 20}, s=60, alpha=.8)

X = df.as_matrix()



# getting data X,y
y = X[:,0]
X = X[:,1:]


#y = y[:].reshape(891,1)
# print X[:2,:]
# print Xy[:2,:]



print X.shape
print y.shape

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)

print("train and test data %s ++ %s ++ %s ++ %s"%(X_train.shape,X_test.shape,y_train.shape,y_test.shape))

from sklearn.linear_model import LogisticRegression

lg = LogisticRegression(C=30)
lg.fit(X_train,y_train)


print " Logistic Regression "
print(" train score is %0.4f"%lg.score(X_train,y_train))
print(" test score is %0.4f"%lg.score(X_test,y_test))

r = np.array([0.01,0.03,0.1,0.3,1,3,10,100])
ac= np.array([])

# for x in range(0,r.size):
#     l = LogisticRegression(C=r[x])
#     l.fit(X_train,y_train)
#     ac = np.append(ac ,l.score(X_test,y_test))
#
# print ac.size
#
# plt.plot(r,ac,'o')
# plt.show()

from sklearn.svm import LinearSVC

clf = LinearSVC(C=0.1)
clf.fit(X_train,y_train)


print " SVM clsf"
print(" train score is %0.4f"%clf.score(X_train,y_train))
print(" test score is %0.4f"%clf.score(X_test,y_test))

from sklearn.svm import SVC
clf = SVC(C=1)
clf.fit(X_train,y_train)
print " SVC  clsf"
print(" train score is %0.4f"%clf.score(X_train,y_train))
print(" test score is %0.4f"%clf.score(X_test,y_test))


# from sklearn.naive_bayes import BernoulliNB
#
# clf1 = BernoulliNB()
# clf1.fit(X_train,y_train)
#
# print " nave bayes "
# print(" train score is %0.4f"%clf1.score(X_train,y_train))
# print(" test score is %0.4f"%clf1.score(X_test,y_test))

# print lg.predict(X_train)
# print y_train

# read final data

data = pd.read_csv('test.csv')
data = data.drop(['Name', 'Ticket', 'Cabin', 'SibSp', 'Parch'], axis=1)
data.Fare.fillna(32.2,inplace=True)

# print data.isnull().sum()

# age add msiisng values

data['Age']=data['Age'].apply(lambda x: np.random.choice([x for x in range(int(min(data['Age'])),int(max(data['Age'])))])if (np.isnan(x)) else x)

data['Sex'] = le1.transform(list(data['Sex'].values))
data['Embarked'] = le2.transform(list(data['Embarked'].values))

T = data.as_matrix()
TX = T[:,1:]
num = T[:,0]

num = num[:].reshape(418,1)

print TX.shape
print num.shape

pred1 = lg.predict(TX)
pred = pred1[:].reshape(418,1)
print pred.shape

final = np.concatenate((num,pred),axis=1)

# print num
# print pred
final = final.astype(int)
#
# print final

np.savetxt("ans.csv",final,delimiter=',')

a77 = pd.read_csv('a77.csv')
aMat = a77.drop(['PassengerId'],axis=1).as_matrix()

aMat = aMat[:,0]

sq = np.square(pred1-aMat)

print np.sum(sq)

print pred1.shape
print aMat.shape

#********************************************************************#
#_______________PLOTING   DATA ______________________________________#

import seaborn as sns

sns.barplot(x='Sex',y='Survived',data=df)
plt.show()


