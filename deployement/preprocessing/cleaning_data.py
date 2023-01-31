import pickle
import json
def preprocess(type,zip_code) :
    if type == "APARTMENT" :
        with open("deployement/model/model_apartement.pickle", "rb") as f:
            model = pickle.load(f)
    elif type == "HOUSE" :
        with open("deployement/model/model_house.pickle", "rb") as f:
            model = pickle.load(f)
    else : 
        return False
    with open("deployement/preprocessing/ZipCode_MeanPrice.json","r") as dicFile : 
            ZipCode_MeanPrice_dict = json.load(dicFile)
    locality = ZipCode_MeanPrice_dict[str(zip_code)]
    return locality, model
