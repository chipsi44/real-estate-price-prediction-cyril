from sklearn.preprocessing import StandardScaler
import numpy as np
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def normalize_scale(df) :
    # Extract all columns except the second one (Price) and assign it to the variable X, and the second column (Price) is assigned to the variable y.
    X = df.drop('Price',axis=1)
    y = df["Price"]

    # Create the StandardScaler object
    scaler = StandardScaler()

    # Fit the scaler to the feature data
    scaler.fit(X)

    # Transform the feature data using the scaler
    X_scaled = scaler.transform(X)

    return X_scaled,y

def training_testing_sets(pandas_data) :
    X_scaled,y = normalize_scale(pandas_data)
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def model_training(pandas_data, model = lambda : LinearRegression()) : 
    X_train, X_test, y_train, y_test = training_testing_sets(pandas_data)
    # fit the model to the training data
    model.fit(X_train, y_train)
    return model

    