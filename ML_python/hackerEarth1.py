import numpy as np
import pandas as pd

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')


train.info()
#print  train.head()


# the missing values in data
nans = train.shape[0] - train.dropna().shape[0]
testnans = test.shape[0] - train.dropna().shape[0]

print('train nans %d -- test %d'%(nans,testnans))


#per coloumn no of null values
train.isnull().sum()

#unique values from col
cat = train.select_dtypes(include=['O'])
cat.apply(pd.Series.nunique)


#Education
# counts of each value of the col
train.workclass.value_counts(sort=True)
# fill the na value with private
train.workclass.fillna('Private',inplace=True)

#Occupation
train.occupation.value_counts(sort=True)
train.occupation.fillna('Prof-specialty',inplace=True)


#Native Country
train['native.country'].value_counts(sort=True)
train['native.country'].fillna('United-States',inplace=True)

#print train.isnull().sum()

# influence the target value in the other columns
pd.crosstab(train.education, train.target,margins=True)/train.shape[0]

from sklearn import  preprocessing

#convert the string into numeric object
for x in train.columns:
    if train[x].dtype == 'object':
        lbl = preprocessing.LabelEncoder()
        lbl.fit(list(train[x].values))
        train[x] = lbl.transform(list(train[x].values))


print (train.head())
#print train.target.value_counts()

