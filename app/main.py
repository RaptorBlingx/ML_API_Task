# main.py
from app.database import engine   # Use app.database, as database.py is in the app directory
from database.models import Base  # Ensure you correctly import Base for table creation
from fastapi import FastAPI
from app.endpoints import upload_data, train_model, predict

from fastapi import FastAPI

app = FastAPI()

# Create the tables
Base.metadata.create_all(bind=engine)

app.include_router(upload_data.router)
app.include_router(train_model.router)
app.include_router(predict.router)



@app.get("/")
def read_root():
    return {"message": "Welcome to the Sustainable Energy API"}
