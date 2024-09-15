from typing import Optional
from pydantic import BaseModel

class EnergyDataSchema(BaseModel):
    country: str
    year: int
    access_to_electricity: Optional[float] = None
    clean_fuels_for_cooking: Optional[float] = None
    renewable_capacity_per_capita: Optional[float] = None
    financial_flows: Optional[float] = None
    renewable_energy_share: Optional[float] = None
    fossil_fuel_electricity: Optional[float] = None
    nuclear_electricity: Optional[float] = None
    renewable_electricity: Optional[float] = None
    low_carbon_electricity: Optional[float] = None
    energy_consumption_per_capita: Optional[float] = None
    energy_intensity: Optional[float] = None
    co2_emissions: Optional[float] = None
    renewables_primary_energy: Optional[float] = None
    gdp_growth: Optional[float] = None
    gdp_per_capita: Optional[float] = None
    population_density: Optional[float] = None
    land_area: Optional[float] = None
    latitude: float
    longitude: float

    class Config:
        orm_mode = True  # Ensures compatibility with SQLAlchemy
