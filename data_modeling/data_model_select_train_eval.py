from sklearn.metrics import accuracy_score,mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from data_modeling.data_formatting import training_testing_sets
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
import pandas as pd

def model_training(model,X_train, X_test, y_train, y_test) : 
    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Predict on the testing data
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print("Mean Squared Error: ", mse)
    print("Mean Absolute Error: ", mae)
    
def test_multiple_model(pandas_data) :    
    # Initialize the model
    
    X_train, X_test, y_train, y_test = training_testing_sets(pandas_data)
    dic_model = {
        "linear_regression": lambda : LinearRegression(),
        "nn" : lambda : MLPRegressor(hidden_layer_sizes=(100, 100, 100), max_iter=2500),
        "ridge": lambda : Ridge(),
        "elastic_net": lambda : ElasticNet(),
        "lasso": lambda : Lasso(),
        "decision_tree": lambda : DecisionTreeRegressor()
    }
    for key, value in dic_model.items() : 
        model = value()
        print(f'started the {key} model')
        model_training(model,X_train, X_test, y_train, y_test)


