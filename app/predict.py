import pandas as pd
from app.utils import preprocess_features_with_names

def predict_price(model, features_dict):
    """
    Predicts the price using a trained model and a dictionary of input features.
    Args:
        model: A trained machine learning model with a `predict` method.
        features_dict (dict): A dictionary containing feature names and their corresponding values.
    Returns:
        float: The predicted price, rounded to two decimal places.
    """

    input_df = pd.DataFrame([preprocess_features_with_names(features_dict)])
    prediction = model.predict(input_df)[0]
    return round(prediction, 2)
