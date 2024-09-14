from sqlalchemy import Column, Integer, Float, String, JSON, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# EnergyData model (maps to energy_data table)
class EnergyData(Base):
    __tablename__ = 'energy_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    access_to_electricity = Column(Float)
    clean_fuels_for_cooking = Column(Float)
    renewable_capacity_per_capita = Column(Float)
    financial_flows = Column(Float)
    renewable_energy_share = Column(Float)
    fossil_fuel_electricity = Column(Float)
    nuclear_electricity = Column(Float)
    renewable_electricity = Column(Float)
    low_carbon_electricity = Column(Float)
    energy_consumption_per_capita = Column(Float)
    energy_intensity = Column(Float)
    co2_emissions = Column(Float)
    renewables_primary_energy = Column(Float)
    gdp_growth = Column(Float)
    gdp_per_capita = Column(Float)
    population_density = Column(Float)
    land_area = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)

# Predictions model (maps to predictions table)
class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    predicted_value = Column(Float, nullable=False)
    model_version = Column(String(50), nullable=False)
    input_data = Column(JSON, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())
