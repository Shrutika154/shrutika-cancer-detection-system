from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle
import os

app = Flask(__name__)
CORS(app)

# ================================
# LOAD MODEL & SCALER (Render Safe)
# ================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")

model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))

# ================================
# PREDICTION API
# ================================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["features"]        # Read input features
        data = np.array(data).reshape(1, -1)   # Convert to array
        data_scaled = scaler.transform(data)   # Scale inputs
        prediction = model.predict(data_scaled)[0]

        result = "Benign (No Cancer)" if prediction == 1 else "Malignant (Cancer Detected)"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

# ================================
# RUN FLASK SERVER
# ================================
if __name__ == "__main__":
    app.run(debug=True)
