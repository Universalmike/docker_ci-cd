# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

class IrisInput(BaseModel):
    features: list

app = FastAPI()
model = joblib.load("models/iris.pkl")

@app.get("/")
def read_root():
    return {"message": "FastAPI app is running!"}

@app.post("/predict")
def predict(data: IrisInput):
    input_data = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])}


