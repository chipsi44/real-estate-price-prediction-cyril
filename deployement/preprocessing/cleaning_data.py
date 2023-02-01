import pickle
import json
# This code defines a function called "preprocess" that takes 3 inputs: type, zip_code, and Number_bedrooms.
def preprocess(type,zip_code,Number_bedrooms) :
    # checks if the type input is equal to "APARTMENT" and loads the appropriate model.
    if type == "APARTMENT" :
        with open("deployement/model/model_apartement.pickle", "rb") as f:
            model = pickle.load(f)
    # checks if the type input is equal to "HOUSE" and loads the appropriate model.
    elif type == "HOUSE" :
        with open("deployement/model/model_house.pickle", "rb") as f:
            model = pickle.load(f)

    # opens a JSON file containing information about the mean price of properties in different zip codes.
    with open("deployement/preprocessing/ZipCode_MeanPrice.json","r") as dicFile : 
            ZipCode_MeanPrice_dict = json.load(dicFile)
    # checks if the zip code input is present in the dictionary of mean prices.
    if str(zip_code) not in ZipCode_MeanPrice_dict.keys() :
        return False, False
    locality = ZipCode_MeanPrice_dict[str(zip_code)]

    # checks if the number of bedrooms input is within the range of 0 to 10.
    if not (0 < Number_bedrooms < 10):
        return False,False

    # If all checks have passed, the function returns the locality and model information.
    return locality, model

