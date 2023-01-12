from data_cleaning import pandas_data
import pandas as pd
import matplotlib.pyplot as plt

df_object = pandas_data('data_cleaned.csv')
df_data = df_object.pandas_data

def is_there_fireplace_here(df_data) :
    # Count the number of houses with fireplaces
    fireplace_count = df_data[df_data['fire_place'] == 1].shape[0]
    #count the number of houses who said they don't have a fire place
    no_info_fireplace_count = df_data[df_data['fire_place'] == 0].shape[0]
    # Count the number of houses without fireplaces
    no_fireplace_count = len(df_data) - fireplace_count

    # Create the bar plot
    plt.bar(['Fireplace', 'No Fireplace',"No info"], [fireplace_count, no_info_fireplace_count,no_fireplace_count])
    plt.xlabel("FirePlace")
    plt.ylabel("Number of Houses")
    plt.show()