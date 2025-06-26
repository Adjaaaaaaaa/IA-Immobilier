import pandas as pd
from app.utils import preprocess_features_with_names

def predict_price(model, features_dict):
    input_df = pd.DataFrame([preprocess_features_with_names(features_dict)])
    prediction = model.predict(input_df)[0]
    return round(prediction, 2)
