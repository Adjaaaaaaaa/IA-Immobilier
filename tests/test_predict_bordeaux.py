from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_bordeaux_valid():
    response = client.post("/predict/bordeaux", json={
        "surface_bati": 120,
        "nombre_pieces": 5,
        "type_local": "Appartement",
        "surface_terrain": 0,
        "nombre_lots": 2
    })
    assert response.status_code == 200
    data = response.json()
    assert "prix_m2_estime" in data
    assert data["ville_modele"] == "Bordeaux"
