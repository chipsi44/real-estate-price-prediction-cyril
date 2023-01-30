from flask import Flask, request, render_template
from sklearn.linear_model import LinearRegression
from model_preparation import model_training
import pandas as pd
import pickle

try:
    pandas_data = pd.read_csv('load_data.csv')
    my_model = model_training(pandas_data)
except Exception as e:
    print("An error occurred while loading the data or training the model:", str(e))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        print("From get")
        return render_template("index.html")
    else:
        print("From Post")
        try:
            locality = int(request.form["locality"])
            Number_bedrooms = float(request.form["Number_bedrooms"])
            Living_area = float(request.form["Living_area"])
            
            prediction = my_model.predict([[locality, Number_bedrooms, Living_area]])
            
            
            return render_template("index.html", prediction=format(prediction[0], ',.2f') + " €")
        except ValueError:
            return render_template("index.html", error_message="Invalid input")

app.run(debug=False)