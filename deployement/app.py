from flask import Flask, request
from sklearn.linear_model import LinearRegression
from model_preparation import model_training
import pandas as pd
import pickle

pandas_data = pd.read_csv('load_data.csv')
my_model = model_training()

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict(model):
    data = request.get_json()
    locality = data["locality"]
    Number_bedrooms = data["Number_bedrooms"]
    Living_area = data["Living_area"]
    
    prediction = model.predict([[locality, Number_bedrooms, Living_area]])
    
    return {"price": prediction[0]}