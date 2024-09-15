# ML_API_Task: Machine Learning API for Sustainable Energy Data

This project is a FastAPI-based machine learning application that trains a model to predict sustainable energy-related metrics using global energy data. The project includes a machine learning model (e.g., XGBoost) integrated into a RESTful API, using PostgreSQL as the database for data storage. 

## Features

- Upload global energy data to the PostgreSQL database
- Train a machine learning model (XGBoost) to predict energy-related metrics
- Make predictions via a FastAPI endpoint
- Store and manage data using PostgreSQL

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [API Endpoints](#api-endpoints)
- [Database Setup](#database-setup)
- [Training the Model](#training-the-model)
- [Making Predictions](#making-predictions)
- [Acknowledgements](#acknowledgements)

---

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- **Python 3.8+**
- **PostgreSQL** (with `pgAdmin` or equivalent to manage the database)
- **Docker** (optional, for containerization)
- **Git** (for version control)

### Python Libraries
The following Python libraries are required and will be installed through `requirements.txt`:

- FastAPI
- numpy
- matplotlib
- Uvicorn
- SQLAlchemy
- XGBoost
- joblib
- python-multipart
- scikit-learn
- pandas
- psycopg2 (for PostgreSQL)

---

## Project Setup

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```
git clone <REPO_URL>
cd ML_API_Task
```

### Step 2: Set Up a Virtual Environment (Recommended)

Create and activate a Python virtual environment to isolate dependencies:

```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (Linux/Mac)
source venv/bin/activate
```

### Step 3: Install Dependencies

Install all the required Python packages using `requirements.txt`:

```
pip install -r requirements.txt
```

### Step 4: Set Up PostgreSQL Database

1. **Create a PostgreSQL database**:
   - Use `pgAdmin` or the PostgreSQL command line to create a new database called `sustainable_energy_db`.
   
   Example SQL command:
   ```
   CREATE DATABASE sustainable_energy_db;
   ```

2. **Update the database URL in `app/database.py`**:
   Update the `DATABASE_URL` in the `app/database.py` file to match your PostgreSQL credentials:

   ```
   DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/sustainable_energy_db"
   ```

### Step 5: Initialize the Database Tables

Run the FastAPI application to create the necessary tables in PostgreSQL:

```
uvicorn app.main:app --reload
```

This will create tables for storing the energy data and model predictions.

---

## Usage

### Running the API

To start the FastAPI application, run the following command from the project directory:

```
uvicorn app.main:app --reload
```

The API will be accessible at: `http://127.0.0.1:8000/`.

### API Endpoints

1. **Upload Data**: `POST /upload-data`
   - Upload a CSV file containing global energy data to store it in the PostgreSQL database.

   **Request**:
   ```
   curl -X POST "http://127.0.0.1:8000/upload-data" -F "file=@path/to/your/file.csv"
   ```

2. **Train Model**: `POST /train-model`
   - Trains a machine learning model on the uploaded data using XGBoost and stores the trained model.

   **Request**:
   ```
   curl -X POST "http://127.0.0.1:8000/train-model"
   ```

3. **Predict**: `POST /predict`
   - Makes predictions using the trained model based on input features (e.g., `fossil_fuel_electricity`, `gdp_per_capita`).

   **Request**:
   ```
   curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{
     "country": "United States",
     "year": 2020,
     "features": {
       "fossil_fuel_electricity": 300,
       "gdp_per_capita": 65000,
       "energy_intensity": 1.4,
       "co2_emissions": 5000
     }
   }'
   ```

---

## Database Setup

The project uses **PostgreSQL** to store energy data and predictions. You will need to:

1. Create a database named `sustainable_energy_db`.
2. Ensure your `app/database.py` is configured with the correct PostgreSQL credentials.
3. Use the `/upload-data` endpoint to populate the `energy_data` table with your dataset.

---

## Training the Model

Once the data is uploaded, you can train the model via the `/train-model` endpoint.

The model is an XGBoost regressor that predicts metrics such as renewable energy share based on various input features (e.g., `fossil_fuel_electricity`, `gdp_per_capita`, etc.).

---

## Making Predictions

After training, you can make predictions using the `/predict` endpoint. The model expects a set of input features and returns a predicted value based on the trained data.

Ensure the model has been trained before making predictions.

---

## Acknowledgements

- FastAPI for the web framework.
- XGBoost for the machine learning model.
- PostgreSQL for data storage.
- Pandas for data manipulation.


---
