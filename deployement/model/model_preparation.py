from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle
import pandas as pd
def training_testing_sets(pandas_data) :
    X_scaled = pandas_data.drop('Price',axis=1)
    y = pandas_data["Price"]
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def model_training(pandas_data, model = LinearRegression()) : 
    X_train, X_test, y_train, y_test = training_testing_sets(pandas_data)
    # fit the model to the training data
    model.fit(X_train, y_train)
    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Calculate the mean absolute error
    mae = mean_absolute_error(y_test, y_pred)

    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)

    # Calculate the R2 score
    r2 = r2_score(y_test, y_pred)

    # Print the results
    print("Mean Absolute Error:", mae)
    print("Mean Squared Error:", mse)
    print("R2 Score:", r2)
    return model



def to_pickle():
    # Your trained model
    pandas_data = pd.read_csv('deployement/model/load_data_apartement.csv')
    my_model = model_training(pandas_data)

    # Export the model to a pickle file
    with open('deployement/model/model_apartement.pickle', 'wb') as file:
        pickle.dump(my_model, file)
    pandas_data = pd.read_csv('deployement/model/load_data_house.csv')
    my_model = model_training(pandas_data)

    # Export the model to a pickle file
    with open('deployement/model/model_house.pickle', 'wb') as file:
        pickle.dump(my_model, file)

to_pickle()