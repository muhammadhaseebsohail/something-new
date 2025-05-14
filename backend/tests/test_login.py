Sure, here are some comprehensive unit tests for the FastAPI endpoint:

```python
from fastapi.testclient import TestClient
import pytest
from your_module import app  # replace 'your_module' with the actual module name

client = TestClient(app)

# Test login endpoint
def test_login_success():
    response = client.post("/login", headers={"Authorization": "Basic dGVzdDp0ZXN0"})
    assert response.status_code == 200
    assert response.json() == {"message": "Logged in successfully"}

def test_login_failure():
    response = client.post("/login", headers={"Authorization": "Basic dGVzdDpwYXNzd29yZA=="})  # username: test, password: password
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect username or password"}

# Test forgot-password endpoint
def test_forgot_password():
    response = client.post("/forgot-password", json={"email": "test@email.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Password reset link has been sent to test@email.com"}

def test_forgot_password_invalid_email():
    response = client.post("/forgot-password", json={"email": "not_an_email"})
    assert response.status_code == 422
    assert "email" in response.json()["detail"][0]["loc"]

# Test create-account endpoint
def test_create_account():
    response = client.post("/create-account", json={"username": "newuser", "password": "newpass", "email": "newuser@email.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Account created successfully"}

def test_create_account_invalid_input():
    response = client.post("/create-account", json={"username": "newuser", "password": "newpass", "email": "not_an_email"})
    assert response.status_code == 422
    assert "email" in response.json()["detail"][0]["loc"]

# Edge case: username or password is empty
def test_login_empty_username_password():
    response = client.post("/login", headers={"Authorization": "Basic Og=="})  # username: "", password: ""
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect username or password"}
```

The tests cover success cases, error cases, data validation (using invalid emails), and an edge case (empty username and password). In a real-world application, you would also want to add tests for the service layer and database models.