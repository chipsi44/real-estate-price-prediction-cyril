import pandas
class pandas_data :
    def __init__(self,file) :
        self.file_name = file
        self.pandas_data = pandas.read_csv(file)
    def clean_price(self) : 
        #Cleaning all the prices that are wrong (Some prices where duplicated) house for 300K was listed as 300 000 300 000
        for position,price in enumerate(self.pandas_data['Price']) :
            if price > 10**9 : 
                mid_len = len(str(price)) / 2
                new_price = str(price)[:int(mid_len)]
                self.pandas_data.at[position,'Price'] = int(new_price)

