import pytest
import uuid

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.main import app
from app.db.base import Base
from app.db.session import get_db
from app.core.config import settings
from app.core.logging_config import logger

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="session")
def auth_headers():
    user_data = {
        "username": "testuser",
        "password": "password123"
    }
    client.post("/api/user/", json=user_data)

    response = client.post("/api/login", data=user_data)
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    return headers

def test_create_school(auth_headers):
    data_school = {
        "name": "Universidad de la Ciudad",
        "country": "Mexico",
        "state": "CDMX",
        "description": "La mejor escuela del mundo mundial",
    }
    response = client.post("/api/schools/", json=data_school, headers=auth_headers)
    logger.debug(response.__dict__)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == data_school["name"]
    assert "id" in data


def test_read_schools(auth_headers):
    response = client.get("/api/schools/", headers=auth_headers)
    logger.debug(response.__dict__)
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_read_school(auth_headers):
    school_id = client.post(
        "/api/schools/",
        json={
            "name": "Universidad de la pueblo",
            "country": "Francia",
            "state": "Paris",
            "description": "La mejor escuela del mundo europeo",
        }, headers=auth_headers
    ).json()["id"]
    response = client.get(f"/api/schools/{school_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == school_id


def test_update_school(auth_headers):
    school_id = client.post(
        "/api/schools/",
        json={
            "name": "Escuela lejana",
            "country": "Muy Lejano",
            "state": "Lejos",
            "description": "Escuela que esta donde da vuelta el aire",
        }, headers=auth_headers
    ).json()["id"]
    response = client.put(
        f"/api/schools/{school_id}",
        json={
            "name": "Escuela cerca",
            "country": "Muy cerca",
            "state": "Cerquita",
            "description": "Escuela que esta donde pasando la calle",
        }, headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Escuela cerca"


def test_delete_school(auth_headers):
    school_id = client.post(
        "/api/schools/",
        json={
            "name": "Escuela",
            "country": "cerca",
            "state": "Aqui",
            "description": "Escuela que esta aqui",
        }, headers=auth_headers
    ).json()["id"]
    response = client.delete(f"/api/schools/{school_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == school_id
    # Verify that the school is actually deleted
    response = client.get(f"/api/schools/{school_id}", headers=auth_headers)
    assert response.status_code == 404
