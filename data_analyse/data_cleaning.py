import pandas as pd
class pandas_data :
    def __init__(self,file) :
        '''
        file : str, path to the file of data
        '''    

        self.file_name = file
        self.pandas_data = pd.read_csv(file)
        #Hard coded it ! TO be faster
        self.dic_ref = {'apartment': 0, 'mixed-use-building': 1, 'house': 2, 'exceptional-property': 3, 'duplex': 4, 'flat-studio': 5,
         'villa': 6, 'country-cottage': 7, 'apartment-block': 8, 'chalet': 9, 'penthouse': 10, 'town-house': 11, 'bungalow': 12, 
         'manor-house': 13, 'farmhouse': 14, 'castle': 15, 'ground-floor': 16, 'mansion': 17, 'other-property': 18, 'triplex': 19, 
         'loft': 20, 'kot': 21, 'service-flat': 22, 'pavilion': 23, 'for-sale': 24, 'Good': 25, 'To be done up': 26, 
         'To renovate': 27, 'As new': 28, 'To restore': 29, 'Just renovated': 30}
        #Clean the data
        #self.clean_price()
        #Create a reference dictionnary
        #self.get_dic_ref()
        #replace all the none by empty value
        #self.pandas_data = self.pandas_data.replace('None', pd.NA )
    def clean_price(self) : 
        #Cleaning all the prices that are wrong (Some prices where duplicated) house for 300K was listed as 300 000 300 000
        for position,price in enumerate(self.pandas_data['Price']) :
            if price > 10**9 : 
                mid_len = len(str(price)) / 2
                new_price = str(price)[:int(mid_len)]
                self.pandas_data.at[position,'Price'] = int(new_price)
    def get_dic_ref(self) :
        x = 0
        #Create a dictionnary that take every element in the df that is a Str and replace it by a number linked to a key
        for elem in self.pandas_data : 
            for position,data in enumerate(self.pandas_data[elem]) :
                if data != 'None' and isinstance(data,str):
                    try : 
                        test = int(data)
                    except : 
                        if data not in self.dic_ref.keys() : 
                            self.dic_ref[data] = x 
                            x += 1
                        self.pandas_data.at[position,elem] = self.dic_ref[data]
                       

