import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import confusion_matrix


dt = DecisionTreeClassifier(max_depth=5, min_samples_split=5)


iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)
predicted = dt.predict(x_test)


iris = load_iris()
x = iris.data
y = iris.target

clf = DecisionTreeClassifier()
parameters = {'max_depth':range(1,11), 'min_samples_split':range(2,11), 'min_samples_leaf':range(1,11)}
search = GridSearchCV(clf, parameters)
search.fit(x, y)
best_tree = search.best_estimator_


iris = load_iris()
x = iris.data
y = iris.target

clf = DecisionTreeClassifier()
parameters = {'max_depth':range(1,11), 'min_samples_split':range(2,11), 'min_samples_leaf':range(1,11)}
search = RandomizedSearchCV(clf, parameters)
search.fit(x, y)
best_tree = search.best_estimator_


x = train.drop(['y'], axis=1)
y = train['y']

clf = DecisionTreeClassifier()
parameters = {'max_depth':range(1,11), 'min_samples_split':range(2,11), 'min_samples_leaf':range(1,11)}
search = GridSearchCV(clf, parameters)
search.fit(x, y)
best_tree = search.best_estimator_

predictions = search.predict(test)


conf_matrix = confusion_matrix(y, predictions)