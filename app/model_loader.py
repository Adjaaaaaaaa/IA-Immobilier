import joblib
import os
"""
This module provides functions to load pre-trained machine learning models for different cities
from a serialized file using joblib.
Constants:
    MODEL_PATH (str): The file path to the serialized model file.
Functions:
    load_model_for_lille():
        Loads and returns the "Random Forest Optimized" model for Lille from the model file.
    load_model_for_bordeaux():
        Loads and returns the "Decision Tree" model for Bordeaux from the model file.
"""


MODEL_PATH = os.path.join("models", "model_lille.pkl")

def load_model_for_lille():
    data = joblib.load(MODEL_PATH)
    model = data["models"]["Random Forest Optimized"]
    return model, "Random Forest Optimized"

def load_model_for_bordeaux():
    data = joblib.load(MODEL_PATH)
    model = data["models"]["Decision Tree"]
    return model, "Decision Tree"
