from data_modeling.data_cleaning_modeling import normalize_scale
from sklearn.model_selection import train_test_split

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
    