from data_aquisition.scrapper import get_urls_from_scrapper
from data_aquisition.data_analyse_pandas import data_to_csv
from data_analyse.data_cleaning import pandas_data
from data_modeling.data_cleaning_modeling import no_duplicates,no_strong_corr,only_great_line, drop_outliers,ZipCode_AveragePrice
from data_modeling.data_model_select_train_eval import test_multiple_model
from threading import RLock
import threading
import time
import pandas as pd

lock = RLock()
 
def main() :
    #Create the CSV link file
    get_urls_from_scrapper()
    # DO THE SCRAPPER TAKE : 40MIN / You need to have your CSV link file.
    threads_list = []
    with open('immo_data.csv', 'w') as data_file : 
        data_file.write('locality,Price,Type_property,Sale_type,Number_bedrooms,Living_area,fully_equipped_kitchen,Furnished,terrace,garden,surface_land,surface_area_plot,facades_number,Swimming_pool,building_state,fire_place\n')
    len_file = 60000
    x = 0 
    while x < len_file : 
        thread = threading.Thread(target = data_to_csv,args =(x,))
        threads_list.append(thread)
        x += 50
    for t in threads_list : 
        t.start()
        time.sleep(0.5)
    for tt in threads_list : 
        tt.join()
    
    # CREATE DATA_CLEANED.CSV take : 30SEC
    
    cleaned_csv = pandas_data("immo_data.csv")
    cleaned_csv.pandas_data.to_csv("data_cleaned.csv", index=False)
    
    #Get results for different model
    pandas_data = pd.read_csv('data_cleaned.csv')
    #Only keep the house for the prediciton
    pandas_data = pandas_data[pandas_data['Type_property'] == 2]
    pandas_data = ZipCode_AveragePrice(pandas_data)
    pandas_data = no_duplicates(pandas_data)
    pandas_data = only_great_line(pandas_data)
    pandas_data = no_strong_corr(pandas_data)
    pandas_data = drop_outliers(pandas_data)
    #OutPut value in the readme
    test_multiple_model(pandas_data)

if __name__ == '__main__' :
    main()
