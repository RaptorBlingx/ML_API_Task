import joblib
import pandas as pd

# Function to load the trained model
def load_model(model_path='D:/ML_API_Task/models/trained_model.pkl'):
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Function to save the trained model
def save_model(model, model_path='D:/ML_API_Task/models/trained_model.pkl'):
    try:
        joblib.dump(model, model_path)
        print("Model saved successfully.")
    except Exception as e:
        print(f"Error saving model: {e}")

# Function to make predictions
def predict(model, input_data):
    try:
        # Convert input data to DataFrame if necessary
        if not isinstance(input_data, pd.DataFrame):
            input_data = pd.DataFrame([input_data])
        predictions = model.predict(input_data)
        return predictions
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None
