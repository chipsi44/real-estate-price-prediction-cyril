from data_cleaning_modeling import no_duplicates, only_great_line, no_strong_corr
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

from data_formatting import training_testing_sets

pandas_data = pd.read_csv('data_cleaned.csv')
pandas_data = no_duplicates(pandas_data)
pandas_data = only_great_line(pandas_data)
pandas_data =  no_strong_corr(pandas_data)

X_train, X_test, y_train, y_test = training_testing_sets(pandas_data)

# Initialize the model
model = LogisticRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Predict on the testing data
y_pred = model.predict(X_test)

# Calculate the train test score
train_score = model.score(X_train, y_train)
test_score = accuracy_score(y_test, y_pred)

print("Train score: ", train_score)
print("Test score: ", test_score)