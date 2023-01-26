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
def most_influence_price(df):
    df = df[['locality','Price','Type_property','Number_bedrooms','Living_area','fire_place']]
    df.dropna()
    #calculating correlation between the price column and all other columns
    corr = df.corr()
    corr_price = corr['Price']
    
    #sorting the correlation values and getting the top 10 highest correlated values
    corr_price = corr_price.sort_values(ascending=False)
    top_corr = corr_price.iloc[1:11]
    
    # Creating a heatmap
    plt.figure(figsize=(10,8))
    plt.title('Top 5 columns influencing price')
    plt.xlabel('Columns')
    plt.ylabel('Correlation')
    plt.imshow(top_corr.values.reshape(1,-1), cmap='Reds', vmin=-1, vmax=1)
    plt.xticks(range(len(top_corr)), top_corr.index, rotation=45)
    plt.colorbar()
    plt.show()



