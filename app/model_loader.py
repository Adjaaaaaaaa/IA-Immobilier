import joblib
import os

MODEL_PATH = os.path.join("models", "model_lille.pkl")

def load_model_for_lille():
    data = joblib.load(MODEL_PATH)
    model = data["models"]["Random Forest Optimized"]
    return model, "Random Forest Optimized"

def load_model_for_bordeaux():
    data = joblib.load(MODEL_PATH)
    model = data["models"]["Decision Tree"]
    return model, "Decision Tree"
