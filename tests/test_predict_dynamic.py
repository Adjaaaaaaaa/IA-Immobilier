from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_dynamic_lille():
    response = client.post("/predict", json={
        "ville": "lille",
        "features": {
            "surface_bati": 90,
            "nombre_pieces": 3,
            "type_local": "Maison",
            "surface_terrain": 30,
            "nombre_lots": 1
        }
    })
    assert response.status_code == 200
    assert response.json()["ville_modele"] == "Lille"

def test_predict_dynamic_invalid_city():
    response = client.post("/predict", json={
        "ville": "paris",  # invalide par rapport à Literal["lille", "bordeaux"]
        "features": {
            "surface_bati": 90,
            "nombre_pieces": 3,
            "type_local": "Maison",
            "surface_terrain": 30,
            "nombre_lots": 1
        }
    })
    assert response.status_code == 422  
