from data_cleaning import pandas_data
import matplotlib.pyplot as plt

df_object = pandas_data('test.csv')
my_df = df_object.pandas_data
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

DPS_histo(my_df)