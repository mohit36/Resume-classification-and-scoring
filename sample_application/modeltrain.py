from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.plotting import plot_confusion_matrix
# example of making multiple probability predictions
from sklearn.linear_model import LinearRegression
from sklearn.datasets.samples_generator import make_blobs
# generate 2d classification dataset
#
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
nb=MultinomialNB()
# example of making multiple probability predictions
df = pd.read_csv(r"allresumes.csv")
df=df.sort_values(['p_id'])
df=df.fillna(0)
true_p = df[((df['accuracy']>=80) & (df['Status'] =="completed")) ]
true_p=true_p[['accuracy','Status']]
true_p=true_p['accuracy'].count()
print(true_p)
true_n = df[((df['accuracy']>=80) & (df['Status'] !="completed")) ]
true_n=true_n[['accuracy','Status']]
true_n=true_n['accuracy'].count()
print(true_n)
key=df['p_id'].count()
false_p = df[((df['accuracy']<80) & (df['Status'] =="parsed with error")) ]
false_p=false_p[['accuracy','Status']]
false_p=false_p['accuracy'].count()
print(false_p)
false_n = df[((df['accuracy']<80) & (df['Status'] !="parsed with error")) ]
false_n=false_n[['accuracy','Status']]
false_n =false_n['accuracy'].count()
print(false_n)
precision=(true_p/(true_p+true_n))
recall=true_p/key
print("here",precision,recall)
d2 = df[['Status']]
total=df['accuracy'].count()
X = np.array(true_p)
y=d2
# Fixing random state for reproducibility

df[df['Status'].notnull()]['Status'].value_counts().plot(kind = 'pie', autopct='%1.1f%%')
#plt.title('status Partitions')
#plt.show()

print(df[['Status', 'accuracy']][df.Status.notnull()].groupby('Status').mean())
df[df['Status'] != 'None'].boxplot(column = ['accuracy'], by = ['Status'])
plt.title('')
plt.show()
ax = sns.boxplot(x="Status", y="accuracy", hue="Status",data=df, linewidth=2.5)
plt.show()
X = np.array(d1)
y=df['Status'] = df['Status'].map({'completed': 1, 'parsed with error': 2,'drop case': 0})


sns.regplot(X, y, data=df, fit_reg=False)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Create data
import seaborn as sns
import matplotlib.pyplot as plt
carrier_count = df['accuracy'].value_counts()
sns.set(style="darkgrid")
sns.barplot(carrier_count.index, carrier_count.values, alpha=0.9)

plt.title('Frequency Distribution of Carriers')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('accuracy', fontsize=12)
plt.show()
# Create plot

#
# df.insert(14, 'predicated_lable', '')
# df
# Sample from a normal distribution using numpy's random number generator

# X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)
# print(X,y)
# fit final model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)
plt.title('Status v/s accuracy')
plt.scatter(X_train, y_train)
plt.plot(X_train, model.predict(X_train))
plt.show()
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# # try:
#     from sklearn.naive_bayes import GaussianNB
#
#     gnb = GaussianNB().fit(X_train, y_train)
#     gnb_predictions = gnb.predict(X_test)
#
#     # accuracy on X_test
#     accuracy = gnb.score(X_test, y_test)
#     print(accuracy)
#
#     # creating a confusion matrix
#     cm = confusion_matrix(y_test, gnb_predictions)
#     print("cm:",cm)
#     fig, ax = plot_confusion_matrix(conf_mat=cm)
#     plt.show()
# except:
#     print("naive bayes fails")
#     # training a KNN classifier
# try:
#     from sklearn.neighbors import KNeighborsClassifier
#
#     knn = KNeighborsClassifier(n_neighbors=7).fit(X_train, y_train)
#
#     # accuracy on X_test
#     accuracy = knn.score(X_test, y_test)
#     print("accuracy:",accuracy)
#
#     # creating a confusion matrix
#     knn_predictions = knn.predict(X_test)
#     cm = confusion_matrix(y_test, knn_predictions)
#     print(cm)
# except:
#     print("kneighbors fails")
# try:
#     from sklearn.svm import SVC
#
#     svm_model_linear = SVC(kernel='linear', C=1).fit(X_train, y_train)
#     svm_predictions = svm_model_linear.predict(X_test)
#
#     # model accuracy for X_test
#     accuracy = svm_model_linear.score(X_test, y_test)
#     print(accuracy)
#
#     # creating a confusion matrix
#     cm = confusion_matrix(y_test, svm_predictions)
#     print(cm)
# except:
#     print("svm fails")
#     # dividing X, y into train and test data
try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # training a DescisionTreeClassifier
    from sklearn.tree import DecisionTreeClassifier

    dtree_model = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
    dtree_predictions = dtree_model.predict(X_test)

    # creating a confusion matrix
    cm = confusion_matrix(y_test, dtree_predictions)
    print(cm)
    from sklearn.tree import DecisionTreeRegressor

    regressor = DecisionTreeRegressor(random_state=1)
    regressor.fit(X_train, y_train)

    # TODO: Report the score of the prediction using the testing set

    # score = cross_val_score(regressor, X_test, y_test)
    score = regressor.score(X_test, y_test)

    print(score)  # python 2.x
    y = np.array(y)
    plot_decision_regions(X, y, clf=svm_model_linear, res=0.02,
                          legend=2, X_highlight=X_test)

    # Adding axes annotations
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Resume classification')
    plt.show()
except:
    print("decesion tree fails")
