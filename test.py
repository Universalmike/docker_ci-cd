from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_endpoint():
    # Example features from Iris dataset
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    json_data = response.json()
    
    assert "prediction" in json_data
    assert isinstance(json_data["prediction"], int)

def test_invalid_input():
    # Send wrong input format
    payload = {"features": "wrong_type"}
    
    response = client.post("/predict", json=payload)
    
    # FastAPI should reject this request
    assert response.status_code == 422
