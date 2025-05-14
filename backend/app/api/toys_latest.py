To accomplish this task, we'll create a `GET` endpoint at `/toys/latest` to retrieve the latest toys from the database, and a `GET` endpoint at `/toys/search` to handle search queries.

Let's start by creating a FastAPI app and the necessary Pydantic and database models:

```python
from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Boolean, Column, Integer, String, DateTime, desc
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import databases, sqlalchemy

# Database config
DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)
Base = declarative_base()

# SQLAlchemy model
class Toy(Base):
    __tablename__ = "toys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime, index=True)

# Pydantic models
class ToyBase(BaseModel):
    name: str
    description: str

class ToyCreate(ToyBase):
    pass

class Toy(ToyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
```

Now let's create the API endpoints:

```python
@app.get("/toys/latest", response_model=List[Toy])
async def read_latest_toys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve the latest toys from the database."""
    toys = db.query(Toy).order_by(desc(Toy.created_at)).offset(skip).limit(limit).all()
    return toys

@app.get("/toys/search", response_model=List[Toy])
async def search_toys(q: str, db: Session = Depends(get_db)):
    """Search for toys based on a query string."""
    toys = db.query(Toy).filter(Toy.name.contains(q)).all()
    return toys
```

Finally, let's create some unit tests for these endpoints:

```python
from fastapi.testclient import TestClient

def test_read_latest_toys():
    response = client.get("/toys/latest")
    assert response.status_code == 200
    assert "id" in response.json()[0]
    assert "name" in response.json()[0]
    assert "description" in response.json()[0]
    assert "created_at" in response.json()[0]

def test_search_toys():
    response = client.get("/toys/search?q=test")
    assert response.status_code == 200
    assert "id" in response.json()[0]
    assert "name" in response.json()[0]
    assert "description" in response.json()[0]
    assert "created_at" in response.json()[0]
```

Note: In a real-world application, you would also want to add error handling and logging, as well as authentication and authorization where needed.