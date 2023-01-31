from sklearn.preprocessing import StandardScaler
import numpy as np
from scipy.stats import zscore
import json
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
    columns_to_keep = ['locality', 'Price','Number_bedrooms', 'Living_area']
    #drop all columns that are not in the list
    df = pandas_data[columns_to_keep]
    df = df.dropna()
    df = df[df.Price < 1000000]
    df = df[df.Number_bedrooms > 0]
    return df 
def drop_outliers(pandas_data) :
    drop_outliers_from = ['Price','Number_bedrooms', 'Living_area']
    for col in drop_outliers_from:
        z_scores = zscore(pandas_data[col])
        filtered_entries = (z_scores.between(-3, 3, inclusive=False))
        pandas_data = pandas_data[filtered_entries]
    return pandas_data


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
def ZipCode_AveragePrice(df_sell):
   # Group the data by the 'locality' column and calculate the mean of the 'Price' column
    df_grouped = df_sell.groupby('locality')['Price'].mean()

    # Replace the values in the 'locality' column with the mean 'Price' value for each 'locality'
    df_sell['locality'] = df_sell['locality'].replace(df_grouped)

    # Convert the grouped data to a dictionary
    output_dict = df_grouped.to_dict()

    # Open a file for writing and write the dictionary to it in JSON format
    with open("output.json", "w") as f:
        json.dump(output_dict, f)

    # Return the original data frame with the modified 'locality' column
    return df_sell

    
