from flask import Flask, request
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # 🔥 THIS LINE FIXES THE ERROR

# load trained model
model = joblib.load("sales_forecast_model.pkl")

@app.route("/")
def home():
    return "Flask is working!"

@app.route("/predict")
def predict():
    store = int(request.args.get("store"))
    promo = int(request.args.get("promo"))
    holiday = int(request.args.get("holiday"))
    day = int(request.args.get("day"))
    month = int(request.args.get("month"))
    dow = int(request.args.get("dow"))

    data = pd.DataFrame({
        'store': [store],
        'promo': [promo],
        'holiday': [holiday],
        'day': [day],
        'month': [month],
        'day_of_week': [dow]
    })

    prediction = model.predict(data)[0]
    return f"Predicted sales: {prediction}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
