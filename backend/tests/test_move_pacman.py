```python
from fastapi.testclient import TestClient
from main import app, Pacman, Ghost, Pellet, Direction

client = TestClient(app)

# Success cases
def test_move_pacman_success():
    response = client.post("/move_pacman/", json={"x": 5, "y": 5, "direction": "up"})
    assert response.status_code == 200

def test_move_ghost_success():
    response = client.post("/move_ghost/", json={"x": 5, "y": 5, "direction": "down"})
    assert response.status_code == 200

def test_eat_pellet_success():
    response = client.post("/eat_pellet/", json={"x": 5, "y": 5})
    assert response.status_code == 200

# Error cases
def test_move_pacman_error():
    response = client.post("/move_pacman/", json={"x": 5, "y": 5, "direction": "diagonal"}) # Not a valid direction
    assert response.status_code == 422

def test_move_ghost_error():
    response = client.post("/move_ghost/", json={"x": 5, "y": 5, "direction": "diagonal"}) # Not a valid direction
    assert response.status_code == 422

def test_eat_pellet_error():
    response = client.post("/eat_pellet/", json={"x": "five", "y": "five"}) # Not valid integers
    assert response.status_code == 422

# Data validation
def test_pacman_data_validation():
    pacman = Pacman(x=5, y=5, direction="up")
    assert pacman.x == 5
    assert pacman.y == 5
    assert pacman.direction == "up"

def test_ghost_data_validation():
    ghost = Ghost(x=5, y=5, direction="down")
    assert ghost.x == 5
    assert ghost.y == 5
    assert ghost.direction == "down"

def test_pellet_data_validation():
    pellet = Pellet(x=5, y=5)
    assert pellet.x == 5
    assert pellet.y == 5

# Edge cases
def test_move_pacman_edge():
    response = client.post("/move_pacman/", json={"x": 0, "y": 0, "direction": "left"}) # Pacman at the edge, trying to move out of the grid
    assert response.status_code == 422

def test_move_ghost_edge():
    response = client.post("/move_ghost/", json={"x": 0, "y": 0, "direction": "left"}) # Ghost at the edge, trying to move out of the grid
    assert response.status_code == 422

def test_eat_pellet_edge():
    response = client.post("/eat_pellet/", json={"x": 0, "y": 0}) # Pellet at the edge of the grid
    assert response.status_code == 200
```

Remember that the edge case tests will only pass if the application is designed to handle such situations. Right now, they would fail as there are no boundary checks implemented in the application.