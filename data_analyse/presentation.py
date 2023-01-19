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
def terrace_property(df) :
    '''
    df : pandas data frame
    '''
    # Select rows where the 'Terrace' column contains a value
    terraced_properties = df[df["terrace"].notnull()]

    # Count the types of properties with a terrace
    property_counts = terraced_properties["Type_property"].value_counts()

    # Print the results
    print(property_counts)

    # Create a bar chart of the property counts
    property_counts.plot(kind='bar')

    # Add a title
    plt.title("Type of property with terrace")

    # Show the chart
    plt.show()

