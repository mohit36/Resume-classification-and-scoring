from sklearn import metrics
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
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import classes

df = pd.read_csv(r"allresumes.csv")
df=df.sort_values(['p_id'])
df=df.fillna(0)
# # importing required modules
# import PyPDF2
#
# # creating a pdf file object
# pdfFileObj = open(r'C:\Users\lenovo\Downloads\SampleCVs\Jignesh_Resume.pdf', 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(pdfReader.numPages)
#
# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracting text from page
# documents=[pageObj.extractText()]
# print(documents)
#
# # closing the pdf file object
# pdfFileObj.close()
# lower_case_documents = []
# for i in documents:
#     lower_case_documents.append(i.lower())
# print(lower_case_documents)
# sans_punctuation_documents = []
# import string
#
# for i in lower_case_documents:
#     sans_punctuation_documents.append(i.translate(str.maketrans('', '', string.punctuation)))
# print(sans_punctuation_documents)
# preprocessed_documents = []
# for i in sans_punctuation_documents:
#     preprocessed_documents.append(i.split(' '))
# print(preprocessed_documents)
#
# frequency_list = []
# import pprint
# from collections import Counter
#
# for i in preprocessed_documents:
#     frequency_counts = Counter(i)
#     frequency_list.append(frequency_counts)
# pprint.pprint(frequency_list)
# from sklearn.feature_extraction.text import CountVectorizer
# count_vector = CountVectorizer()
# print(count_vector)
# count_vector.fit(documents)
# count_vector.get_feature_names()
#
# doc_array = count_vector.transform(documents).toarray()
# doc_array
# frequency_matrix = pd.DataFrame(doc_array,
#                                 columns = count_vector.get_feature_names())

# Instantiate the CountVectorizer method
# count_vector = CountVectorizer()

# Fit the training data and then return the matrix
# training_data = count_vector.fit_transform(X_train)

# Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
# testing_data = count_vector.transform(X_test)
df=df.sort_values(['p_id'])
feature_cols = ['accuracy']
X = df[feature_cols]
X =df.iloc[:,1]
X=X.values.reshape(-1,1)
df['Status']= df['Status'].map({'completed': 1, 'parsed with error': 2,'drop case': 0})
# y=df['Pred_accuracy']
y=df['Status']

y=y.values.reshape(-1,1)
# print(y)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    random_state=4)

print('Number of rows in the total set: {}'.format(df.shape[0]))
print('Number of rows in the training set: {}'.format(X_train.shape[0]))
print('Number of rows in the test set: {}'.format(X_test.shape[0]))

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train, y_train)
predictions = naive_bayes.predict(y_test)
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,classification_report
print('Accuracy score: ', format(metrics.accuracy_score(y_test, predictions)))
print('Precision score: ', format(metrics.precision_score(y_test, predictions,average='weighted', labels=np.unique(predictions))))
print('Recall score: ', metrics.recall_score(y_test, predictions, average='weighted', labels=np.unique(predictions)))
print('F1 score: ', format(metrics.f1_score(y_test, predictions, average='weighted', labels=np.unique(predictions))))
print(metrics.f1_score(y_test, predictions, average='weighted', labels=np.unique(predictions)))
df=df.sort_values(['p_id'])
feature_cols = ['accuracy']
X = df[feature_cols]
X =df.iloc[:,1]
X=X.values.reshape(-1,1)
#y= df['Status'].map({'completed': 1, 'parsed with error': 2,'drop case': 0})
y=df['Pred_accuracy']
y=df.iloc[:,2]
print(y)
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
# from sklearn.linear_model import LogisticRegression
# logreg = LogisticRegression()
# logreg.fit(X_train, y_train)
# print(X_train,y_train)
# # make class predictions for the testing set
# y_pred_class = logreg.predict(X_test)
#
# # calculate accuracy
# from sklearn import metrics
# print("accuracy:",metrics.accuracy_score(y_test, y_pred_class))
#
# # examine the class distribution of the testing set (using a Pandas Series method)
# y_test.value_counts()
#
# # calculate the percentage of ones
# y_test.mean()
# # calculate the percentage of zeros
# 1 - y_test.mean()
#
# # calculate null accuracy (for binary classification problems coded as 0/1)
# max(y_test.mean(), 1 - y_test.mean())
# # calculate null accuracy (for multi-class classification problems)
# y_test.value_counts().head(1) / len(y_test)
#
# # print the first 25 true and predicted responses
# print('True:', y_test.values[0:50])
# print('Pred:', y_pred_class[0:50])
#
# # IMPORTANT: first argument is true values, second argument is predicted values
# print("confusion matrix:",metrics.confusion_matrix(y_test, y_pred_class))
#
# print('True:', y_test.values[0:50])
# print('Pred:', y_pred_class[0:50])
#
# confusion = metrics.confusion_matrix(y_test, y_pred_class)
# TP = confusion[1, 1]
# TN = confusion[0, 0]
# FP = confusion[0, 1]
# FN = confusion[1, 0]
#
#
# print((TP + TN) / float(TP + TN + FP + FN))
# print(metrics.accuracy_score(y_test, y_pred_class))
#
# print((FP + FN) / float(TP + TN + FP + FN))
# print(1 - metrics.accuracy_score(y_test, y_pred_class))
#
# print(TP / float(TP + FN))
# print(metrics.recall_score(y_test, y_pred_class,average='weighted'))
#
# print(TN / float(TN + FP))
# print(FP / float(TN + FP))
# print(TP / float(TP + FP))
# print(metrics.precision_score(y_test, y_pred_class,average='weighted'))
#
# logreg.predict(X_test)[0:50]
#
# logreg.predict_proba(X_test)[0:50, :]
# logreg.predict_proba(X_test)[0:50, 1]
# y_pred_prob = logreg.predict_proba(X_test)[:, 1]
# import matplotlib.pyplot as plt
#
# # histogram of predicted probabilities
# plt.hist(y_pred_prob, bins=2)
# plt.xlim(0, 1)
# plt.title('Histogram of predicted probabilities')
# plt.xlabel('Predicted probability of diabetes')
# plt.ylabel('Frequency')
# plt.show()
# from sklearn.preprocessing import binarize
# print(metrics.confusion_matrix(y_test,predictions))
# print(46 / float(46 + 16))
# print(80 / float(80 + 50))
# fpr, tpr, thresholds = metrics.roc_curve(y_test,predictions)
# plt.plot(fpr, tpr)
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.0])
# plt.title('ROC curve for Resume classifier')
# plt.xlabel('False Positive Rate (1 - Specificity)')
# plt.ylabel('True Positive Rate (Sensitivity)')
# plt.grid(True)
# plt.show()

# # define a function that accepts a threshold and prints sensitivity and specificity
# def evaluate_threshold(threshold):
#     print('Sensitivity:', tpr[thresholds > threshold][-1])
#     print('Specificity:', 1 - fpr[thresholds > threshold][-1])
#
# evaluate_threshold(0.5)
#
# evaluate_threshold(0.3)
df=df[['accuracy','Pred_accuracy']]
print(df)

# TODO: Import 'r2_score'
from sklearn.metrics import r2_score


def performance_metric(y_true, y_predict):
    """ Calculates and returns the performance score between
        true and predicted values based on the metric chosen. """

    # TODO: Calculate the performance score between 'y_true' and 'y_predict'
    score = r2_score(y_true, y_predict)

    # Return the score
    return score
score = performance_metric(X[:20], y[:20])
print("Model has a coefficient of determination, R^2, of {:.3f}.".format(score))
# TODO: Import 'train_test_split'
from sklearn.model_selection import train_test_split
# TODO: Shuffle and split the data into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=4)
print(X_train)
# Success
print("Training and testing split was successful.")
import visuals as vs
vs.ModelLearning(X, y)
plt.show()

vs.ModelComplexity(X_train, y_train)
plt.show()

from sklearn.metrics import make_scorer
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ShuffleSplit


def fit_model(X, y):
    """ Performs grid search over the 'max_depth' parameter for a
        decision tree regressor trained on the input data [X, y]. """

    # Create cross-validation sets from the training data
    # sklearn version 0.18: ShuffleSplit(n_splits=10, test_size=0.1, train_size=None, random_state=None)
    # sklearn versiin 0.17: ShuffleSplit(n, n_iter=10, test_size=0.1, train_size=None, random_state=None)
    cv_sets = ShuffleSplit(X.shape[0], test_size=0.20, random_state=101)

    # TODO: Create a decision tree regressor object
    regressor = DecisionTreeRegressor()

    # TODO: Create a dictionary for the parameter 'max_depth' with a range from 1 to 10
    params = {'max_depth': range(1, 10)}

    # TODO: Transform 'performance_metric' into a scoring function using 'make_scorer'

    scoring_fnc = make_scorer(performance_metric)

    # TODO: Create the grid search cv object --> GridSearchCV()
    # Make sure to include the right parameters in the object:
    # (estimator, param_grid, scoring, cv) which have values 'regressor', 'params', 'scoring_fnc', and 'cv_sets' respectively.
    grid = GridSearchCV(estimator=regressor, param_grid=params, scoring=scoring_fnc, cv=cv_sets, refit=True)

    # Fit the grid search object to the data to compute the optimal model
    grid = grid.fit(X, y)

    # Return the optimal model after fitting the data
    return grid.best_estimator_
# Fit the training data to the model using grid search
reg = fit_model(X_train, y_train)

# Produce the value for 'max_depth'
print("Parameter 'max_depth' is {} for the optimal model.".format(reg.get_params()['max_depth']))
