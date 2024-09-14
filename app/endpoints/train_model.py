# app/endpoints/train_model.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from database.models import EnergyData
from models.model_utils import save_model
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import pandas as pd

router = APIRouter()

@router.post("/train-model")
async def train_model(db: Session = Depends(get_db)):
    # Query the data from the energy_data table
    data = db.query(EnergyData).all()

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame([{
        "country": d.country,
        "year": d.year,
        "renewable_energy_share": d.renewable_energy_share,
        "fossil_fuel_electricity": d.fossil_fuel_electricity,
        "gdp_per_capita": d.gdp_per_capita,
        "energy_intensity": d.energy_intensity,
        "co2_emissions": d.co2_emissions
    } for d in data])

    # Check for missing or invalid values in the label (target) column
    # Drop rows where the label (renewable_energy_share) is NaN or infinity
    df = df.dropna(subset=['renewable_energy_share'])  # Remove rows with NaN in the target column
    df = df[~df['renewable_energy_share'].isin([float('inf'), float('-inf')])]  # Remove rows with infinity values

    # Define your features and target variable
    X = df[['fossil_fuel_electricity', 'gdp_per_capita', 'energy_intensity', 'co2_emissions']]
    y = df['renewable_energy_share']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model (using XGBoost as an example)
    model = XGBRegressor()
    model.fit(X_train, y_train)

    # Save the trained model
    save_model(model, "models/trained_model.pkl")

    return {"message": "Model trained successfully."}
