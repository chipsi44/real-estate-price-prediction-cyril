from sklearn.preprocessing import StandardScaler
import numpy as np


'''

No text data -> already done

'''
# No duplicates -> Precision it's not real duplicate, it's different immo that have the same caracteristique
def no_duplicates(pandas_data) : 
    pandas_data = pandas_data.drop_duplicates()
    if pandas_data[pandas_data.duplicated()].empty : 
        print("Done ! No duplicates")
    return pandas_data
#No NANs
def only_great_line(pandas_data) :
    # list of desired columns
    columns_to_keep = ['locality', 'Price', 'Type_property','Number_bedrooms', 'Living_area']
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

def normalize_scale(df) :
    # Extract the feature columns (all columns except the first one)
    X = df.iloc[:, 1:]
    y = df.iloc[:, 0]
    # Create the StandardScaler object
    scaler = StandardScaler()

    # Fit the scaler to the feature data
    scaler.fit(X)

    # Transform the feature data using the scaler
    X_scaled = scaler.transform(X)
    return X_scaled,y