from data_cleaning_modeling import no_duplicates, only_great_line, no_strong_corr
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,mean_squared_error, mean_absolute_error
from data_formatting import training_testing_sets
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
import pandas as pd

def model_training(model,X_train, X_test, y_train, y_test) : 
    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Predict on the testing data
    y_pred = model.predict(X_test)

    # Calculate the train test score
    train_score = model.score(X_train, y_train)
    if isinstance(model, (LinearRegression, MLPRegressor)):
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        print("Mean Squared Error: ", mse)
        print("Mean Absolute Error: ", mae)
    else : 
        test_score = accuracy_score(y_test, y_pred)
        print("Train score: ", train_score)
        print("Test score: ", test_score)
def test_multiple_model(pandas_data) :    
    # Initialize the model
    
    X_train, X_test, y_train, y_test = training_testing_sets(pandas_data)
    dic_model = {
        "linear_regression": lambda : LinearRegression(),
        "logistic" : lambda : LogisticRegression(),
        "random_forest": lambda : RandomForestClassifier(),
        #"svm": lambda : SVC(),
        "nn" : lambda : MLPRegressor(hidden_layer_sizes=(100, 100, 100), max_iter=2500)
    }
    for key, value in dic_model.items() : 
        model = value()
        print(f'started the {key} model')
        model_training(model,X_train, X_test, y_train, y_test)


pandas_data = pd.read_csv('data_cleaned.csv')
pandas_data = no_duplicates(pandas_data)
pandas_data = only_great_line(pandas_data)
pandas_data =  no_strong_corr(pandas_data)
test_multiple_model(pandas_data)