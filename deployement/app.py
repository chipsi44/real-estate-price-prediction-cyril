from flask import Flask, request, render_template
import pandas as pd
import pickle

with open("deployement/model.pickle", "rb") as f:
    model = pickle.load(f)

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
            
            prediction = model.predict([[locality, Number_bedrooms, Living_area]])
            
            
            return render_template("index.html", prediction=format(prediction[0], ',.2f') + " €")
        except ValueError:
            return render_template("index.html", error_message="Invalid input")

app.run(debug=False)