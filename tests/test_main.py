# Importation des librairies
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_homepage():
    response = client.get("/home")
    assert response.status_code == 200
    assert response.json()== {"Status": "OK"}