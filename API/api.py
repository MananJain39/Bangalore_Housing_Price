from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import json
import numpy as np

app = FastAPI()

with open('BHP_using_RFR.pickle', 'rb') as f:
    model = pickle.load(f)

with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']


@app.get("/")
def root():
    return {"message": "Bangalore House Price Prediction API is running!"}


class PredictionRequest(BaseModel):
    bhk: int
    total_sqft: float
    bath: int
    location: str

@app.post('/predict')
def PredictionPrice(data: PredictionRequest):
    try:
        input_data = np.zeros(len(data_columns))
        input_data[0] = data.bhk
        input_data[1] = data.total_sqft
        input_data[2] = data.bath

        loc = data.location.lower()
        if loc in data_columns:
            loc_index = data_columns.index(loc)
            input_data[loc_index] = 1

        prediction = model.predict([input_data])[0]
        return {'estimated_price': round(prediction, 2)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
