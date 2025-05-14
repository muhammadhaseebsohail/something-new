Let's start by creating the Pydantic models for the request and response data. We'll need models for login, forgotten password, and account creation.

```python
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class ForgottenPasswordRequest(BaseModel):
    email: str

class AccountCreationRequest(BaseModel):
    username: str
    password: str
    email: str

class ResponseModel(BaseModel):
    message: str
```

Next, we'll create a service layer that handles the business logic of authentication. In a real-world application, this would interact with a database and use encryption for passwords, but for simplicity, we'll use a dummy implementation.

```python
from fastapi import HTTPException
from passlib.context import CryptContext

class AuthenticationService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def authenticate_user(self, username: str, password: str):
        # In real-world application, you should fetch user from database
        # Here we use a dummy user for demonstration
        dummy_user = {"username": "test", "password": self.get_password_hash("test")}
        
        if username != dummy_user["username"]:
            return False
        if not self.verify_password(password, dummy_user["password"]):
            return False
        return True

    def create_user(self, username: str, password: str, email: str):
        # In a real-world application, this would involve creating a new user in the database.
        return {"username": username, "password": self.get_password_hash(password), "email": email}

    def forgot_password(self, email: str):
        # In a real-world application, this would involve sending a password reset email to the user.
        return {"message": f"Password reset link has been sent to {email}"}
```

Now, we'll create the FastAPI application and the endpoints.

```python
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()
app = FastAPI()

auth_service = AuthenticationService()

@app.post("/login", response_model=ResponseModel)
def login(credentials: HTTPBasicCredentials = Depends(security)):
    """Verify username and password"""
    if not auth_service.authenticate_user(credentials.username, credentials.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"message": "Logged in successfully"}

@app.post("/forgot-password", response_model=ResponseModel)
def forgot_password(request: ForgottenPasswordRequest):
    """Handle forgotten password"""
    return auth_service.forgot_password(request.email)

@app.post("/create-account", response_model=ResponseModel)
def create_account(request: AccountCreationRequest):
    """Handle account creation"""
    return auth_service.create_user(request.username, request.password, request.email)
```

Here is a sample unit test for the login endpoint:

```python
from fastapi.testclient import TestClient

def test_login():
    client = TestClient(app)
    response = client.post("/login", headers={"Authorization": "Basic dGVzdDp0ZXN0"})
    assert response.status_code == 200
    assert response.json() == {"message": "Logged in successfully"}
```

Note that the `Authorization` header is the base64 encoding of the string "test:test", which corresponds to the dummy user in the `AuthenticationService`.