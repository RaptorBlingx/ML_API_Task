# app/endpoints/upload_data.py

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
import pandas as pd
from sqlalchemy.orm import Session
from app.database import get_db
from database.models import EnergyData

router = APIRouter()

@router.post("/upload-data")
async def upload_data(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file.file)

        # Sanitize column names: replace newline characters and strip extra spaces
        df.columns = df.columns.str.replace(r'\n', ' ', regex=True).str.strip()

        # Remove commas from numeric columns and convert them to float
        numeric_columns = ['access_to_electricity', 'clean_fuels_for_cooking', 'renewable_capacity_per_capita',
                           'financial_flows', 'renewable_energy_share', 'fossil_fuel_electricity', 
                           'nuclear_electricity', 'renewable_electricity', 'low_carbon_electricity', 
                           'energy_consumption_per_capita', 'energy_intensity', 'co2_emissions', 
                           'renewables_primary_energy', 'gdp_growth', 'gdp_per_capita', 'population_density', 
                           'land_area', 'latitude', 'longitude']

        # Replace commas and convert the columns to float
        for col in numeric_columns:
            if col in df.columns:
                df[col] = df[col].replace({',': ''}, regex=True).astype(float)

        # Insert data into the energy_data table
        for _, row in df.iterrows():
            energy_data = EnergyData(
                country=row['Entity'],
                year=row['Year'],
                access_to_electricity=row['Access to electricity (% of population)'],
                clean_fuels_for_cooking=row['Access to clean fuels for cooking'],
                renewable_capacity_per_capita=row['Renewable-electricity-generating-capacity-per-capita'],
                financial_flows=row['Financial flows to developing countries (US $)'],
                renewable_energy_share=row['Renewable energy share in the total final energy consumption (%)'],
                fossil_fuel_electricity=row['Electricity from fossil fuels (TWh)'],
                nuclear_electricity=row['Electricity from nuclear (TWh)'],
                renewable_electricity=row['Electricity from renewables (TWh)'],
                low_carbon_electricity=row['Low-carbon electricity (% electricity)'],
                energy_consumption_per_capita=row['Primary energy consumption per capita (kWh/person)'],
                energy_intensity=row['Energy intensity level of primary energy (MJ/$2017 PPP GDP)'],
                co2_emissions=row['Value_co2_emissions_kt_by_country'],
                renewables_primary_energy=row['Renewables (% equivalent primary energy)'],
                gdp_growth=row['gdp_growth'],
                gdp_per_capita=row['gdp_per_capita'],
                population_density=row['population_density'],
                land_area=row['Land Area(Km2)'],
                latitude=row['Latitude'],
                longitude=row['Longitude']
            )
            db.add(energy_data)
        db.commit()
        
        return {"message": "Data uploaded successfully."}

    except Exception as e:
        print(f"Error occurred: {e}")  # Log the error to console
        raise HTTPException(status_code=500, detail="Internal server error")
