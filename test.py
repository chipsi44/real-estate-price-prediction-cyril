import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.stats import zscore
import numpy as np
from data_modeling.data_cleaning_modeling import normalize_scale
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from data_modeling.data_formatting import training_testing_sets
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
'''

No text data -> already done

'''
# No duplicates -> Precision it's not real duplicate, it's different immo that have the same caracteristics
def no_duplicates(pandas_data) : 
    pandas_data = pandas_data.drop_duplicates()
    if pandas_data[pandas_data.duplicated()].empty : 
        print("Done ! No duplicates")
    return pandas_data
#No NANs
def only_great_line(pandas_data) :
    # list of desired columns
    columns_to_keep = ['locality','Price','Number_bedrooms', 'Living_area']
    #drop all columns that are not in the list
    df = pandas_data[columns_to_keep]
    df = df.dropna()
    return df 

#No features that have too strong correlation between them
def no_strong_corr(pandas_data) : 
    # Compute the correlation matrix
    corr_matrix = pandas_data.corr()

    # Get the absolute value of the correlation coefficients
    corr_matrix = corr_matrix.abs()

    # Set the diagonal elements to nan
    corr_matrix = corr_matrix.where(np.triu(np.ones(corr_matrix.shape)).astype(bool))
    
    # drop the diagonal elements
    corr_matrix = corr_matrix.dropna()

    # Print the correlations that are greater than a certain threshold
    threshold = 0.8
    
    
    to_drop = []

    for col in corr_matrix.columns :
        if any(corr_matrix[col] > threshold) :
            to_drop.append(col)
    to_drop = to_drop[1:]

    pandas_data = pandas_data.drop(to_drop, axis=1)
    return pandas_data

#Use data normalization / scaling

def normalize_scale(X) :
    # Extract all columns except the second one (Price) and assign it to the variable X, and the second column (Price) is assigned to the variable y.
    #X = df.drop('Price',axis=1)
    #y = df["Price"]

    # Create the StandardScaler object
    scaler = StandardScaler()

    # Fit the scaler to the feature data
    scaler.fit(X)

    # Transform the feature data using the scaler
    X_scaled = scaler.transform(X)

    #return X_scaled,y
    return X_scaled
def drop_outliers(pandas_data) :
    drop_outliers_from = ['Price','Number_bedrooms', 'Living_area']
    for col in drop_outliers_from:
        z_scores = zscore(pandas_data[col])
        filtered_entries = (z_scores.between(-3, 3, inclusive=False))
        pandas_data = pandas_data[filtered_entries]
    return pandas_data


def model_training(model,X_train, X_test, y_train, y_test) : 
   # fit the model to the training data
    model.fit(X_train, y_train)

    # evaluate the model on the test data
    score = model.score(X_test, y_test)
    print(f'Test score: {score:.2f}')
    
    # make predictions
    y_pred = model.predict(X_test)
    
    # calculate MAE and MSE
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    # print the results
    print(f'Test Mean Absolute Error: {mae:.2f}')
    print(f'Test Mean Squared Error: {mse:.2f}')
def test_multiple_model(pandas_data) :    
    # Initialize the model
    
    X_train, X_test, y_train, y_test = training_testing_sets(pandas_data)
    dic_model = {
        "linear_regression": lambda : LinearRegression(),
        "ridge": lambda : Ridge(),
        "elastic_net": lambda : ElasticNet(),
        "lasso": lambda : Lasso(),
        "decision_tree": lambda : DecisionTreeRegressor(),
        #"nn" : lambda : MLPRegressor(hidden_layer_sizes=(100, 100, 100), max_iter=2500)
    }
    for key, value in dic_model.items() : 
        model = value()
        print(f'started the {key} model')
        model_training(model,X_train, X_test, y_train, y_test)


def training_testing_sets(pandas_data) :
    #X_scaled,y = normalize_scale(pandas_data)
    X = pandas_data.drop('Price',axis=1)
    y = pandas_data["Price"]
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train = normalize_scale(X_train)
    X_test = normalize_scale(X_test)

    return X_train, X_test, y_train, y_test

def ZipCode_AveragePrice(df_sell) :

    df_sell['locality'] = df_sell['locality'].replace(df_sell.groupby('locality')['Price'].mean())
    print(df_sell)
    return df_sell

def try_knn(pandas_data) :
    X = pandas_data.drop('Price',axis=1)
    y = pandas_data["Price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=21)
   
    
    knn.fit(X_train, y_train)
    # use the model to make predictions on the test data
    y_pred = knn.predict(X_test)

    # evaluate the model's performance
    # calculate MAE and MSE
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    # print the results
    print(f'Test Mean Absolute Error: {mae:.2f}')
    print(f'Test Mean Squared Error: {mse:.2f}')



pandas_data = pd.read_csv('data_cleaned.csv')
pandas_data = pandas_data[pandas_data['Type_property'] == 2]
pandas_data = only_great_line(pandas_data)
pandas_data = pandas_data[pandas_data.Price < 1000000]
pandas_data = pandas_data[pandas_data.Number_bedrooms > 0]
pandas_data = ZipCode_AveragePrice(pandas_data)
pandas_data = drop_outliers(pandas_data)
print(pandas_data)
test_multiple_model(pandas_data)