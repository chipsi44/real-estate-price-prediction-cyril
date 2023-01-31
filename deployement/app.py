from flask import Flask, request, render_template
from math import sqrt
import pandas as pd
import pickle
import json

#appartements = 0
#House = 2 

with open("deployement/model.pickle", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        print("ALIVE")
        return render_template("index.html")
    else:
        print("From Post")
        with open("deployement/ZipCode_MeanPrice.json","r") as dicFile : 
            ZipCode_MeanPrice_dict = json.load(dicFile)
        try:
            locality = int(request.form["locality"])
            locality = ZipCode_MeanPrice_dict[str(locality)]
            
            Number_bedrooms = float(request.form["Number_bedrooms"])
            Living_area = float(request.form["Living_area"])
            
            prediction = model.predict([[locality, Number_bedrooms, Living_area]])
            
            
            return render_template("index.html", prediction=format(prediction[0], ',.2f') + " €")
        except ValueError:
            return render_template("index.html", error_message="Invalid input")

app.run(debug=False)