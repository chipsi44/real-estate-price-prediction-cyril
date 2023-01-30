from flask import Flask, request
from sklearn.linear_model import LinearRegression
from model_preparation import model_training
import pandas as pd
import pickle

pandas_data = pd.read_csv('load_data.csv')
my_model = model_training(pandas_data)


app = Flask(__name__)

@app.route("/", methods=["POST"])
def predict(model):

    #data = request.get_json()
    data = {
        "locality" : 4000,
        "Number_bedrooms" : 4.0,
        "Living_area" : 180.0
    }
    locality = data["locality"]
    Number_bedrooms = data["Number_bedrooms"]
    Living_area = data["Living_area"]
    
    prediction = model.predict([[locality, Number_bedrooms, Living_area]])
    
    return {"price": prediction[0]}

app.run(debug=False)