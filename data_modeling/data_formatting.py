from data_modeling.data_cleaning_modeling import normalize_scale
from sklearn.model_selection import train_test_split

def training_testing_sets(pandas_data) :
    X_scaled,y = normalize_scale(pandas_data)
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def ZipCode_AveragePrice(df) :
    zip_code_dic = {}
    for zip_code,position in enumerate(df['locality']) :
        if zip_code not in zip_code_dic.keys() :
            zip_code_dic = {zip_code : []}
        zip_code_dic[zip_code].append(df['Price'][position])
    print(zip_code_dic)