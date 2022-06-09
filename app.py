#libraries
import numpy as np
from flask import Flask, request, render_template
import pickle
import sklearn

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
#home page
@app.route("/")
def home():
    return render_template("index.html")
#prediction page
@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    predict_proba = int(model.predict_proba(features).max()*100)
    return render_template("index.html", prediction_text = "The flower species is {}".format(prediction)+"accuracy of  {} %".format(predict_proba))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)