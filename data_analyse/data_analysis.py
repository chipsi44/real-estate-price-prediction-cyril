
from data_cleaning import pandas_data

df_object = pandas_data('immo_data.csv')
df_object.clean_price()
# How many rows and columns?
def num_rows_cols(df) :
    num_rows = len(df)
    num_col = len(df.columns)
    return num_rows, num_col

print(df_object.pandas_data.corr())