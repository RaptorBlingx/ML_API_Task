# app/endpoints/predict.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from models.model_utils import load_model
from pydantic import BaseModel

router = APIRouter()

class PredictionRequest(BaseModel):
    country: str
    year: int
    features: dict  # You can pass in the necessary features for the model

@router.post("/predict")
async def predict(request: PredictionRequest, db: Session = Depends(get_db)):
    model = load_model()  # Load the trained model

    # Extract features from the request
    features = list(request.features.values())

    # Make prediction
    predicted_value = model.predict([features])[0]

    # Convert the prediction result to a Python float before returning
    return {"predicted_value": float(predicted_value)}
