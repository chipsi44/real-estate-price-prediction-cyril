from data_cleaning import pandas_data
import pandas as pd
import matplotlib.pyplot as plt
from data_analysis import missing_values_percentage

'''
When you take all the data it says that what's influence the most the price is the fire place.
It's because their is not enough data about the fire place. 
I wanted to show it, and explain why it should be a great idea to force people to say if there is a fireplace into their houses.
So it wanted to show how to improve immoweb ! 
'''
def missing_value(df_data) :
    '''
    df_data : pandas data frame 
    '''

    # Calculate the percentage of missing values for each column
    missing_values = missing_values_percentage(df_data)

    # Plot the results as a bar chart
    missing_values.plot(kind='bar')

    # Add labels and show the graph
    plt.title("Missing value by percentage")
    plt.xlabel('Columns')
    plt.ylabel('Percentage of missing values')
    plt.show()

