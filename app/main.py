# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

class IrisInput(BaseModel):
    features: list

app = FastAPI()
model = joblib.load("app/iris.pkl")

@app.post("/predict")
def predict(data: IrisInput):
    input_data = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])}
