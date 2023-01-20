#from data_aquisition.scrapper import get_urls_from_scrapper
from data_aquisition.data_analyse_pandas import data_to_csv
from data_analyse.data_cleaning import pandas_data
from threading import RLock
import threading
import time

lock = RLock()
 
def main() :
    # DO THE SCRAPPER TAKE : 40MIN 
    '''    
    #get_urls_from_scrapper()
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
    '''
    # CREATE DATA_CLEANED.CSV take : 30SEC
    '''
    cleaned_csv = pandas_data("immo_data.csv")
    cleaned_csv.pandas_data.to_csv("data_cleaned.csv")
    '''

    
if __name__ == '__main__' :
    main()
