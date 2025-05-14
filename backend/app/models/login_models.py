The request and response models have already been included in the provided code. Here is a summary of them:

#### Request Models

```python
class LoginRequest(BaseModel):
    username: str
    password: str

class ForgottenPasswordRequest(BaseModel):
    email: str

class AccountCreationRequest(BaseModel):
    username: str
    password: str
    email: str
```

In LoginRequest model, we have `username` and `password` fields.
In ForgottenPasswordRequest model, we have `email` field.
In AccountCreationRequest model, we have `username`, `password`, and `email` fields.

#### Response Model

```python
class ResponseModel(BaseModel):
    message: str
```

In the ResponseModel, we have a `message` field which is a string that will hold a response message.

#### Data Transfer Object

A Data Transfer Object (DTO) is an object that carries data between processes. In our case, the DTOs are the request and response models. They carry the data from the client to the server (in case of a POST request) and from the server to the client (as a response).

For instance, when a client sends a POST request to the "/create-account" endpoint, it sends data in the form of an `AccountCreationRequest` object. This object gets processed in the server and a `ResponseModel` object is returned to the client.

The Pydantic models provided (`LoginRequest`, `ForgottenPasswordRequest`, `AccountCreationRequest`, `ResponseModel`) act as DTOs to validate the data types of the incoming request and the outgoing response.