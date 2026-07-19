import joblib
import pandas as pd
model = joblib.load("Models/fraud_detection_model.pkl")
scaler = joblib.load("Models/scaler.pkl")
def predict_transaction(features):
    """Predict whether a transaction is genuine or fraudulent."""
    columns = [
        "Time",
        "V1", "V2", "V3", "V4", "V5",
        "V6", "V7", "V8", "V9", "V10",
        "V11", "V12", "V13", "V14", "V15",
        "V16", "V17", "V18", "V19", "V20",
        "V21", "V22", "V23", "V24", "V25",
        "V26", "V27", "V28",
        "Amount"
    ]
    data = pd.DataFrame([features], columns=columns)
    data[["Time", "Amount"]] = scaler.transform(data[["Time", "Amount"]])
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    if prediction:
        return "Fraud Transaction", probability
    return "Genuine Transaction", probability