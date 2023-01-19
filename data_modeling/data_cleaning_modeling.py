import pandas as pd
from sklearn.preprocessing import StandardScaler

pandas_data = pd.read_csv('data_cleaned.csv')
#Hard coded it ! TO be faster
dic_ref = {'apartment': 0, 'mixed-use-building': 1, 'house': 2, 'exceptional-property': 3, 'duplex': 4, 
        'flat-studio': 5, 'villa': 6, 'country-cottage': 7, 'apartment-block': 8, 'chalet': 9, 'penthouse': 10, 'town-house': 11, 
        'bungalow': 12, 'manor-house': 13, 'farmhouse': 14, 'castle': 15, 'ground-floor': 16, 'mansion': 17, 'other-property': 18, 
        'triplex': 19, 'loft': 20, 'kot': 21, 'service-flat': 22, 'pavilion': 23, 'for-sale': 24,'Good': 25, 'To be done up': 26,
         'To renovate': 27, 'As new': 28, 'To restore': 29, 'Just renovated': 30}

'''
No NANs -> already done
No text data -> already done

'''
# No duplicates -> Precision it's not real duplicate, it's different immo that have the same caracteristique
def no_duplicates(pandas_data) : 
    pandas_data = pandas_data.drop_duplicates()
    if pandas_data[pandas_data.duplicated()].empty : 
        print("Done ! No duplicates")

#Doesn't work, dunno why
def no_strong_corr(pandas_data) : 
    #No features that have too strong correlation between them

    # Compute the correlation matrix
    corr_matrix = pandas_data.corr()

    # Get the absolute value of the correlation coefficients
    corr_matrix = corr_matrix.abs()

    # Print the correlations that are greater than a certain threshold
    threshold = 0.8

    to_drop = []

    for col in corr_matrix.columns :
        if any(corr_matrix[col] > threshold) :
            to_drop.append(col)
    to_drop = to_drop[1:]

    pandas_data = pandas_data.drop(to_drop, axis=1)

#Use data normalization / scaling

def normalize_scale(df) :
    # Extract the feature columns (all columns except the first one)
    X = df.iloc[:, 1:]

    # Create the StandardScaler object
    scaler = StandardScaler()

    # Fit the scaler to the feature data
    scaler.fit(X)

    # Transform the feature data using the scaler
    X_scaled = scaler.transform(X)
