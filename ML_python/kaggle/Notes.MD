
# Notes Beginner

## Data Refining

### Insights :
- Write basic  observation on data i.e size , type, number
- write for each col its type, missing%,contns or discrete or categorizable
- make some predictions based on data
- group the categorizable data 
- get info from data ie . sex Mr, Mrs from name or age category etc.

### Plotting :
- plot the data for each col vs target and see whats your predictions vs data dependcy
- libraries in python matplotlib and seaborn also pandas.scatterplot and Dataframe.plot
- see if data as imapct as you predicted
- barchart/hist/piechart for discrete and scatterplot / line graph /curve for continus data 
- use grouping to visualise data of grouped typ( age,salary,etc)


### Data cleaning :
- Clean the data by imputing missing values 
- use mean / median / mode for if less %
- use random data from the data if the range is not big and %missing is lil large
- if most of the data missing can drop the col
- replce strings with numerals by mapping it  ( use df[col].map(dict) or LabelEncode sklearn )

### Add new features :
- use the category to add categorised col
- use categorised col to predict missing values
- add new features from combining old ones
- square or multiply 

### MODELS :
- try models with splitting training and test set

### Model Names :
- Gaussian Naive Bayes
- Logistic Regression
- Support Vector Machines
- Perceptron
- Decision Tree Classifier
- Random Forest Classifier
- KNN or k-Nearest Neighbors
- Stochastic Gradient Descent
- Gradient Boosting Classifier


