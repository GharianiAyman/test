from fastapi.testclient import TestClient
from main import app 
client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"name": "Test Task", "description": "Test Description"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Task"
    assert response.json()["description"] == "Test Description"

def test_read_task():
    response = client.get("/task/1") 
    assert response.status_code == 200
    assert response.json()["name"] == "Test Task"
    assert response.json()["description"] == "Test Description"

def test_update_task():
    response = client.put("/task/1", json={ "id":1 , "name": "Updated Task", "description": "Updated Description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Task"
    assert response.json()["description"] == "Updated Description"

def test_delete_task():
    response = client.delete("/task/1") 
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Task"
    assert response.json()["description"] == "Updated Description"
if __name__ == "__main__":
    test_create_task()
    test_read_task()
    test_update_task()
    test_delete_task()