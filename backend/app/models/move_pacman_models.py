The request models are already defined in the code as `Pacman`, `Ghost`, and `Pellet`. Now, let's define the response models. 

```python
from pydantic import BaseModel

class MoveResponse(BaseModel):
    x: int
    y: int
    direction: Optional[str] = None
    status: str

class EatResponse(BaseModel):
    x: int
    y: int
    status: str
```

In these models, `x` and `y` are the new coordinates after the move or eat actions. `direction` is the new direction after the move action, it is optional because it is not needed for the eat action. `status` is the status of the game after the action.

Now let's refactor the endpoints to use these response models with HTTP status codes and proper error handling.

```python
@app.post("/move_pacman/", response_model=MoveResponse)
async def move_pacman(pacman: Pacman):
    """
    This endpoint moves the Pacman.
    """
    # Replace with actual logic
    game_over = False
    if game_over:
        raise HTTPException(status_code=400, detail="Game over")
    else:
        return {"x": pacman.x, "y": pacman.y, "direction": pacman.direction, "status": "Running"}

@app.post("/move_ghost/", response_model=MoveResponse)
async def move_ghost(ghost: Ghost):
    """
    This endpoint moves a ghost.
    """
    # Replace with actual logic
    game_over = False
    if game_over:
        raise HTTPException(status_code=400, detail="Game over")
    else:
        return {"x": ghost.x, "y": ghost.y, "direction": ghost.direction, "status": "Running"}

@app.post("/eat_pellet/", response_model=EatResponse)
async def eat_pellet(pellet: Pellet):
    """
    This endpoint makes the Pacman eat a pellet.
    """
    # Replace with actual logic
    game_over = False
    if game_over:
        raise HTTPException(status_code=400, detail="Game over")
    else:
        return {"x": pellet.x, "y": pellet.y, "status": "Running"}
```

In a real-world application, you would probably want to use custom exceptions for different game over conditions. You could also use FastAPI's dependency injection system to manage game state, instead of assuming it in each endpoint. That way, you could have a single game state that is accessed and modified by all endpoints. This would involve creating a custom class to manage game state and using FastAPI's `Depends` function to inject it into each endpoint.