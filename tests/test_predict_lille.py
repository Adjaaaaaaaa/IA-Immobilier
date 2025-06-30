from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_lille_valid():
    response = client.post("/predict/lille", json={
        "surface_bati": 100,
        "nombre_pieces": 4,
        "type_local": "Maison",
        "surface_terrain": 50,
        "nombre_lots": 1
    })
    assert response.status_code == 200
    data = response.json()
    assert "prix_m2_estime" in data
    assert data["ville_modele"] == "Lille"
