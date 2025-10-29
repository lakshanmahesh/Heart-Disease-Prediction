from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your saved model
with open("model/model.pickle", "rb") as file:
    best_model = pickle.load(file)

# Order of features used by the model
FEATURE_ORDER = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect input values in correct order
        values = []
        for feature in FEATURE_ORDER:
            val = float(request.form[feature])
            values.append(val)

        input_data = np.array([values])
        prediction = best_model.predict(input_data)[0]

        # Human-readable output
        if int(prediction) == 1:
            message = "⚠️ Heart Disease Likely"
            color = "danger"
        else:
            message = "✅ No Heart Disease Detected"
            color = "success"

        inputs = dict(zip(FEATURE_ORDER, values))
        return render_template("result.html", prediction_text=message, color=color, inputs=inputs)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
