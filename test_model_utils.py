from models.model_utils import load_model, save_model, predict
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Test data for prediction
test_input = pd.DataFrame({
    'feature1': [5.1, 4.9],
    'feature2': [3.5, 3.0],
    'feature3': [1.4, 1.4],
    'feature4': [0.2, 0.2]
})

# Create a sample model (RandomForestClassifier in this case)
model = RandomForestClassifier()
model.fit(test_input, [0, 1])  # Dummy fitting just for testing

# Test saving the model
save_model(model)

# Test loading the model
loaded_model = load_model()

# Test predictions
if loaded_model is not None:
    predictions = predict(loaded_model, test_input)
    print(f"Predictions: {predictions}")
else:
    print("Model not loaded, can't test predictions.")
