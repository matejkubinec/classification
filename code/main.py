import pandas as pd

# 1. load data
data_df = pd.read_csv('data.csv', sep=';')

# 2. separete label column
play = data_df['Play']
data_df = data_df.drop('Play', 1)

# 3. preprocessing - categorical columns
cat_cols = ['Outlook', 'Temperature Nominal', 'Humidity Nominal', 'Windy']
data_df = pd.get_dummies(data_df, columns=cat_cols)

# 4. training/testing data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data_df, play, test_size=0.2)

# K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=2)
clf.fit(x_train, y_train)

clf.score(x_test, y_test)

# Decision Tree
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

clf.score(x_test, y_test)

# Neural Networks
from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(hidden_layer_sizes=(3, 5))
clf.fit(x_train, y_train)

clf.score(x_test, y_test)
