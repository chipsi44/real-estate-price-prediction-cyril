from bs4 import BeautifulSoup
from data_aquisition.data_cleaning import reference_dic_needed, clean_escape_characters
from threading import RLock
import requests
import re
import pandas as pd
import random
import csv
import threading
import time

def remove_html_tags(s):
    new_s = re.sub('\s+', ' ', s)
    return re.sub("<[^<]+?>", "", new_s)

def get_data_from_url(url) :
    #get the data from the url
    url_splited = url.split('/')
    bip_boup = url_splited[5:9]
    if bip_boup[0] == "new-real-estate-project-houses" or bip_boup[0] == "new-real-estate-project-apartments" :
        return 'empty'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #get the data we need from the class 'classified-table_data' (wich are the data)
    info = soup.find_all(class_ = 'classified-table__data')
    info_utf8 = str(info).encode('utf-8')
    info_list = str(info_utf8).split('<td class="classified-table__data"')
    #get the data we need from the class 'classified-table_header (wich is the description)
    info = soup.find_all(class_ = 'classified-table__header')
    info_utf8 = str(info).encode('utf-8')
    description_list = str(info_utf8).split('<th class="classified-table__header" scope="row">')
    #get the data from the url
    url_splited = url.split('/')
    bip_boup = url_splited[5:9]
    #get bedrooms and size
    result = ""
    new_result = []
    bedroom = ""
    size_of_house = ""
    for elem in soup.find_all("p", attrs={"class": "classified__information--property"}):
        temp = elem.text
        temp = temp.replace("\n", '')
        temp = temp.replace(" ", '')
        result += temp
        new_result = result.split("|")
        try :
            bedroom = re.sub("[^0-9]", "", new_result[0])
            size_of_house = re.sub("[^0-9]", "", new_result[1])
        except : 
            bedroom = 'None'
            size_of_house = 'None'
    #create the dic
    the_dic = {
        'property_type' : bip_boup[0],
        'sale_type' : bip_boup[1],
       'locality' : bip_boup[3],
       'bedroom' : bedroom,
       'size_of_house' : size_of_house,
    }
    
    #Clean the data
    for description,data in zip(description_list[1:],info_list[1:]) :
        the_dic[remove_html_tags(description)] = remove_html_tags(data)
    #return the data cleaned
    return the_dic

    
def data_to_pandas(data_dic,data_frame) :
    '''
    Parameters:
    data_dic (dict): A dictionary containing the key-value pairs to be added to the dataframe.
    data_frame (pandas.DataFrame): The dataframe to which the key-value pairs from `data_dic` will be added.
    
    Returns:
    pandas.DataFrame: The modified dataframe with the key-value pairs from `data_dic` added.
    '''
    #Adding the none in the list of the key that doesn't match
    len_items = False
    if len(data_frame) > 0 : 
        for key,value in data_frame.items() :
            len_items = len(data_frame[key])
            if key not in data_dic :
                data_frame[key].append('None')
    #Adding the value in the dic, if the key doesn't exist, create a list with x * none at the beginning    
    for key,value in data_dic.items() :
        if key in data_frame :
            data_frame[key].append(value)
        else : 
            data_frame[key] = []
            if len_items : 
                for _ in range(len_items) :
                    data_frame[key].append('None')
            data_frame[key].append(value)
    
    return data_frame

def data_to_csv(pass_row) :
        count = 0
        ploted_frame = {}
        random_num = random.randint(0,50000)
        if random_num == random.randint(0,50000) : 
            time.sleep(0.1)
        with open('links.csv', 'r') as links_file : 
            reader = csv.reader(links_file)
            #Skip the line already in use by other threads
            for i in range(pass_row) :
                next(reader)
            for row in reader :
                the_data = get_data_from_url(row[0])
                if the_data == 'empty' :
                    pass
                else : 
                    ploted_frame = data_to_pandas(the_data,ploted_frame)
                    count += 1
                    print(f"I'm at {count + pass_row} page done")
                if count == 50 : 
                    break
                    
        for key in ploted_frame:
            ploted_frame[key] = [clean_escape_characters(value) for value in ploted_frame[key]]
        ploted_frame = reference_dic_needed(ploted_frame)

        df = pd.DataFrame(ploted_frame)
        
        with lock :
            with open('immo_data.csv','a') as data_file : 
                df.to_csv(data_file, mode='a', header=False, index=False)