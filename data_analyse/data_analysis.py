
from data_cleaning import pandas_data

df_object = pandas_data('test.csv')
# How many rows and columns?
def num_rows_cols(df) :
    num_rows = len(df)
    num_col = len(df.columns)
    return num_rows, num_col
#What is the correlation between the variables and the price?
def corr_with_price(df) :
    return df.corrwith(df['Price'])
#Which variables have the greatest influence on the price?
def most_influence_price(df) :
    '''Since we have a lot of None value for the fireplace or the swiming pool it often return that
    it's the swimming pool or the fire place that influence the most
    Based on my human knowledge I'll only take the columns that make big difference'''
    df_subset = df[['locality','Price','Type_property','Number_bedrooms','Living_area']]
    max = 0
    columns_name = df_subset.columns
    for index,corr_value in enumerate(corr_with_price(df_subset)) :
        if abs(corr_value) > max and corr_value != 1 : 
            max_colums = columns_name[index]
            max = abs(corr_value)
    return max_colums
#Which variables have the least influence on the price?
def less_influence_price(df) :
    '''Since we have a lot of None value for the fireplace or the swiming pool it often return that
    it's the swimming pool or the fire place that influence the most
    Based on my human knowledge I'll only take the columns that make big difference'''
    df_subset = df[['locality','Price','Type_property','Number_bedrooms','Living_area']]
    min = 2
    columns_name = df_subset.columns
    for index,corr_value in enumerate(corr_with_price(df_subset)) :
        if abs(corr_value) < min : 
            min_colums = columns_name[index]
            min = abs(corr_value)
    return min_colums
#What is the percentage of missing values per column?
def missing_values_percentage(df):
  return df.isnull().mean() * 100
print(missing_values_percentage(df_object.pandas_data))