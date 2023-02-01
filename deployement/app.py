from flask import Flask, request, render_template
from preprocessing.cleaning_data import preprocess
from predict.prediction import my_predict

# This code creates a Flask web application.
app = Flask(__name__)

# defines a route that is accessible at the root URL ("/").
@app.route("/", methods=["GET", "POST"])
# This function is executed when a request is made to the root URL.
def predict():
    if request.method == "GET":
        # If the request method is "GET", the string "ALIVE" is printed and the "index.html" template is rendered.
        print("ALIVE")
        return render_template("index.html")
    
    else:
        print("From Post") 
        # The values of the locality, number of bedrooms, living area, and type are extracted from the form data.
        locality = int(request.form["locality"])
        Number_bedrooms = int(request.form["Number_bedrooms"])
        Living_area = float(request.form["Living_area"])
        type = str(request.form['type'])

        # The locality and model are preprocessed using the "preprocess" function defined earlier.
        locality,model = preprocess(type,locality,Number_bedrooms)
        # If the preprocessing function returns False, an error message is passed to the template and rendered.
        if model == False : 
            return render_template("index.html", error_message="Invalid input")

        prediction = my_predict(model,locality,Living_area,Number_bedrooms)
        # The prediction is formatted as a string with two decimal places and the thousands separator (,).
        prediction = "{:,.2f} €".format(prediction[0])
        prediction = prediction.replace(',', ' ')
        # The prediction is passed to the template and rendered.
        return render_template("index.html", prediction = prediction)

app.run(debug=False)
