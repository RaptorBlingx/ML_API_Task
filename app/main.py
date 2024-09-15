import math
import logging
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, get_db
from database.models import Base, EnergyData
from app.schemas import EnergyDataSchema
from app.endpoints import upload_data, train_model, predict
from typing import List

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include other routers
app.include_router(upload_data.router)
app.include_router(train_model.router)
app.include_router(predict.router)

# Set up logging
logging.basicConfig(level=logging.INFO)

def clean_float(value):
    """Replace NaN, infinity, and out-of-range floats with None."""
    if value is None:
        return None
    if isinstance(value, (float, int)) and (math.isnan(value) or math.isinf(value) or abs(value) > 1e308):
        return None
    return value

@app.get("/get-data/{country}", response_model=List[dict])
async def get_data(country: str, db: Session = Depends(get_db)):
    result = db.query(EnergyData).filter(EnergyData.country == country).all()
    
    if not result:
        return {"message": f"No data found for {country}"}
    
    cleaned_data = []
    for row in result:
        row_dict = row.__dict__.copy()
        # Remove SQLAlchemy's internal state
        row_dict.pop('_sa_instance_state', None)
        
        # Handle NaN or None values by replacing them
        for key, value in row_dict.items():
            if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
                row_dict[key] = None  # Replace NaN/inf with None or 0 based on your preference
                
        cleaned_data.append(row_dict)
    
    return cleaned_data
