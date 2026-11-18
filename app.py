
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained machine learning model
with open("SLR_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    height = float(request.form["height"])

    # Convert input into the format expected by the model
    input_data = np.array([[height]])

    # Predict weight
    prediction = model.predict(input_data)[0]

    prediction = round(float(prediction), 2)

    return render_template(
        "index.html",
        prediction_text=f"Predicted Weight: {prediction} kg",
        entered_height=height
    )


if __name__ == "__main__":
    app.run(debug=True)