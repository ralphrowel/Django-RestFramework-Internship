# Status Code Reference for API Testing

# 200 OK                    → Request succeeded (e.g., successful GET, PUT, PATCH, DELETE).
# 201 Created               → A new resource was successfully created (e.g., POST success).
# 204 No Content            → Request succeeded, no response body (common for DELETE).
# 400 Bad Request           → Client error (e.g., invalid data, missing fields).
# 401 Unauthorized          → Missing or invalid authentication (no or wrong token).
# 403 Forbidden             → Authenticated but not allowed (permissions issue).
# 404 Not Found             → Resource doesn’t exist (wrong ID or URL).
# 405 Method Not Allowed    → HTTP method not supported (e.g., using GET on /create/).
# 500 Internal Server Error → Something broke on the server side.

import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from task.models import Order

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_test_user(db):
    return User.objects.create_user(username="ralph", password="March282004.")

# 200 OK  → Request succeeded (e.g., successful GET, PUT, PATCH, DELETE).

@pytest.fixture
def get_access_token(api_client, create_test_user):
    response = api_client.post("/api/token/", {
        "username": "ralph",
        "password": "March282004."
    }, format="json")
    return response.data["access"]

def test_authentication_success(api_client, create_test_user):
    response = api_client.post("/api/token/", {
        "username": "ralph",
        "password": "March282004."
    }, format="json")

    assert response.status_code == 200

    assert "access" in response.data
    assert "refresh" in response.data

# 201 Created → A new resource was successfully created (e.g., POST success).

@pytest.mark.django_db
def test_create_order(api_client, create_test_user):
    api_client.force_authenticate(user=create_test_user)

    url = "/api/task/create/"
    payload = {
        "product": "Laptop",
        "name": "John Doe",
        "price": "1200.00",
        "description": "High-end gaming laptop"
    }

    response = api_client.post(url, payload, format="json")

    assert response.status_code == 201
    assert "id" in response.data
    assert response.data["name"] == "John Doe"


# 400 Bad Request  → Client error (e.g., invalid data, missing fields).

@pytest.mark.django_db
def test_create_order_missing_fields(api_client, create_test_user):
    # Authenticate the client
    api_client.force_authenticate(user=create_test_user)

    url = "/api/task/create/"
    # Missing required field "product"
    payload = {
        "customer_name": "John Doe",
        "quantity": 2
    }

    response = api_client.post(url, payload, format="json")

    assert response.status_code == 400
    assert "product" in response.data

# 401 Unauthorized → Missing or invalid authentication (no or wrong token).

@pytest.mark.django_db
def test_create_order_unauthorized(api_client):
    url = "/api/task/create/"
    payload = {
        "product": "Phone",
        "name": "Jane",
        "price": "600.00",
        "description": "Latest smartphone"
    }

    response = api_client.post(url, payload, format="json")

    assert response.status_code == 401

# 404 Not Found → Resource doesn’t exist (wrong ID or URL).

@pytest.mark.django_db
def test_get_nonexistent_order(api_client, create_test_user, get_access_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {get_access_token}")

    response = api_client.get("/api/orders/99999/") # dito
    assert response.status_code == 404

# 405 Method Not Allowed    → HTTP method not supported (e.g., using GET on /create/).

@pytest.mark.django_db
def test_method_not_allowed(api_client, create_test_user, get_access_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {get_access_token}")

    response = api_client.put("/api/task/create/")
    assert response.status_code == 405
