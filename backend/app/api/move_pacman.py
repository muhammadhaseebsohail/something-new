The task is quite complex and would result in a substantial amount of code, but here's a simplified example of how you might structure your application. 

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from enum import Enum

app = FastAPI()

class Direction(str, Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"

class Pacman(BaseModel):
    x: int
    y: int
    direction: Direction

class Ghost(BaseModel):
    x: int
    y: int
    direction: Direction

class Pellet(BaseModel):
    x: int
    y: int

@app.post("/move_pacman/")
async def move_pacman(pacman: Pacman):
    """
    This endpoint moves the Pacman.
    """
    # Logic to move pacman and check for collisions with walls or ghosts.
    # If collision with ghost, game over. If collision with pellet, eat it.
    # The logic should be implemented here or in a separate service.
    # This is a simplified example, so the logic is omitted.

@app.post("/move_ghost/")
async def move_ghost(ghost: Ghost):
    """
    This endpoint moves a ghost.
    """
    # Logic to move ghost and check for collisions with walls or pacman.
    # If collision with pacman, game over.
    # The logic should be implemented here or in a separate service.
    # This is a simplified example, so the logic is omitted.

@app.post("/eat_pellet/")
async def eat_pellet(pellet: Pellet):
    """
    This endpoint makes the Pacman eat a pellet.
    """
    # Logic to eat pellet and check for all pellets eaten, if so, game over.
    # The logic should be implemented here or in a separate service.
    # This is a simplified example, so the logic is omitted.
```

Unit tests for the endpoints could look like this:

```python
from fastapi.testclient import TestClient

def test_move_pacman():
    with TestClient(app) as client:
        response = client.post("/move_pacman/", json={"x": 5, "y": 5, "direction": "up"})
        assert response.status_code == 200

def test_move_ghost():
    with TestClient(app) as client:
        response = client.post("/move_ghost/", json={"x": 5, "y": 5, "direction": "down"})
        assert response.status_code == 200

def test_eat_pellet():
    with TestClient(app) as client:
        response = client.post("/eat_pellet/", json={"x": 5, "y": 5})
        assert response.status_code == 200
```

In a real-world application, you would probably store the game state in a database and implement more complex game logic. For example, you might have separate services for moving characters and checking game over conditions, or you might use a more sophisticated method for determining the direction of movement.