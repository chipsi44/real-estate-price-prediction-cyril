from data_cleaning_modeling import no_duplicates, normalize_scale, only_great_line
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

pandas_data = pd.read_csv('data_cleaned.csv')
pandas_data = no_duplicates(pandas_data)
pandas_data = only_great_line(pandas_data)
print(pandas_data)
def training_testing_sets(pandas_data) :
    pandas_data = no_duplicates(pandas_data)
    X_scaled,y = normalize_scale(pandas_data)
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

