from data_cleaning import pandas_data
import pandas as pd
import matplotlib.pyplot as plt
from data_analysis import missing_values_percentage

'''
The data suggests that the presence of a fire place has the most significant impact on the price of a property. 
However, it may be due to a lack of data on the topic. To improve the accuracy and completeness of the data, 
it would be beneficial to make it mandatory for property owners or real estate agents to provide information about the presence
of a fire place when listing a property. This would also be beneficial for potential buyers as it would help them make better
decisions based on the features they are looking for. The two graphs presented in the analysis aim to demonstrate the importance
of collecting data about the presence of a fire place and the potential benefits of implementing this requirement on the platform.
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

