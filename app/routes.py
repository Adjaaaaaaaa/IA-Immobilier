from fastapi import FastAPI, HTTPException, APIRouter
from app.schemas import PredictRequest, PredictResponse, DynamicPredictRequest
from app.model_loader import load_model_for_lille, load_model_for_bordeaux
from app.predict import predict_price
router = APIRouter()

@router.post("/predict/lille", response_model=PredictResponse)
def predict_lille(data: PredictRequest):
        model, model_name = load_model_for_lille()
        price = predict_price(model, data.dict())
        return PredictResponse(prix_m2_estime=price, ville_modele="Lille", model=model_name)
    
@router.post("/predict/bordeaux", response_model=PredictResponse)
def predict_bordeaux(data: PredictRequest):
        model, model_name = load_model_for_bordeaux()
        price = predict_price(model, data.dict())
        return PredictResponse(prix_m2_estime=price, ville_modele="Bordeaux", model=model_name)
   

@router.post("/predict", response_model=PredictResponse)
def predict_dynamic(req: DynamicPredictRequest):
        if req.ville == "lille":
            model, model_name = load_model_for_lille()
            ville_label = "Lille"
        elif req.ville == "bordeaux":
            model, model_name = load_model_for_bordeaux()
            ville_label = "Bordeaux"
        else:
            raise HTTPException(status_code=400, detail="Ville non reconnue.")

        price = predict_price(model, req.features.dict())
        return PredictResponse(prix_m2_estime=price, ville_modele=ville_label, model=model_name)

   