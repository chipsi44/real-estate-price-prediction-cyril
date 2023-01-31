from flask import Flask, request, render_template
from preprocessing.cleaning_data import preprocess
from predict.prediction import my_predict

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        print("ALIVE")
        return render_template("index.html")
    else:
        print("From Post")
        
        try:
            locality = int(request.form["locality"])
            Number_bedrooms = float(request.form["Number_bedrooms"])
            Living_area = float(request.form["Living_area"])
            type = str(request.form['type'])
            locality,model = preprocess(type,locality)
            prediction = my_predict(model,locality,Living_area,Number_bedrooms)
            prediction = "{:.2f} €".format(prediction[0])
            
            return render_template("index.html", prediction = prediction)
        except ValueError:
            print('error')
            return render_template("index.html", error_message="Invalid input")

app.run(debug=False)