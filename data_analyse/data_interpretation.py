from data_cleaning import pandas_data
import matplotlib.pyplot as plt
import pandas as pd

#plot the outliers
def plot_outliers(df) :
    plt.figure(1)
    df[['Number_bedrooms']].boxplot()

    plt.figure(2)
    df[['Price']].boxplot()

    plt.figure(3)
    df[['Living_area']].boxplot()

    plt.show()
'''
wich variables would you delete and why, i'd delete the variable that are too high in Price and in living area. 
Because exeptional properties or expetional Price could false the statistic ! Since Immoweb is made for Mrs Mr everybody,
it's better to have "normal" price and all.
'''
#represent the number of properties according to their surface using a histogram
def DPS_histo(df) :
    #Calculate first and third quartile
    q1, q3 = df['Living_area'].quantile([0.25, 0.75])
    #Calculate Interquartile range
    iqr = q3 - q1
    #Heum, thanks to my stats lessons.

    #Filtering out the records that have Living_area outside of 1.5 IQR range. Thanks to chat gpt
    filtered_df = df[(df['Living_area'] > (q1 - 1.5 * iqr)) & (df['Living_area'] < (q3 + 1.5 * iqr))]
    # Create a histogram of the Living_area column. Thanks to my knowledge in matplotlib
    plt.hist(filtered_df['Living_area'])
    # Set the title and labels of the histogram
    plt.title('number of properties according to their surface')
    plt.xlabel("Surface")
    plt.ylabel("Number of properties")
    # Show the histogram
    plt.show()

'''
Wich are the 5 variables are the most important and why : 
'locality','Price','Type_property','Number_bedrooms','Living_area'
Because that's the variables where I have the more data. The more data you have the more accurate the analysis is right ? 
What is the percentage of missing values per column? <- According to the answer of this question
'''
#What are the most expensive municipalities in belgium
def most_exepensive(df) :
    # Group the data by 'locality'
    grouped_df = df.groupby(['locality'])

    # Calculate the mean, median and price per square meter for each group and rename the column to prevent duplication
    #Oke to be honnest this 3 lines, chat gpt helped me a lot 
    mean_price = grouped_df.Price.mean().reset_index().rename(columns={'Price':'Mean Price'})
    median_price = grouped_df.Price.median().reset_index().rename(columns={'Price':'Median Price'})
    price_per_meter = pd.DataFrame(grouped_df.Price.sum()/grouped_df.Living_area.sum(),columns=['Price per square meter']).reset_index()
    
    # Concatenating the dataframes
    result = pd.concat([mean_price, median_price, price_per_meter], axis=1)

    # Sort the dataframe by the mean price in descending order
    result.sort_values(by='Mean Price', ascending=False, inplace=True)

    # Select the top municipalities
    top_municipalities = result.head(10)
    print(top_municipalities)

#What are the most expensive municipalities in belgium
def less_exepensive(df) :
    # Group the data by 'locality'
    grouped_df = df.groupby(['locality'])

    # Calculate the mean, median and price per square meter for each group and rename the column to prevent duplication
    #Oke to be honnest this 3 lines, chat gpt helped me a lot 
    mean_price = grouped_df.Price.mean().reset_index().rename(columns={'Price':'Mean Price'})
    median_price = grouped_df.Price.median().reset_index().rename(columns={'Price':'Median Price'})
    price_per_meter = pd.DataFrame(grouped_df.Price.sum()/grouped_df.Living_area.sum(),columns=['Price per square meter']).reset_index()
    
    # Concatenating the dataframes
    result = pd.concat([mean_price, median_price, price_per_meter], axis=1)

    # Sort the dataframe by the mean price in descending order
    result.sort_values(by='Mean Price', ascending=True, inplace=True)

    # Select the top municipalities
    top_municipalities = result.head(10)
    print(top_municipalities)
df_object = pandas_data('data_cleaned.csv')
df_data = df_object.pandas_data

DPS_histo(df_data)