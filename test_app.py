import pytest
from flask import Flask
from app_service import AppService

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"App Works!!!" in response.data

def test_get_tasks(client):
    appService = AppService()
    expected_response = appService.get_tasks()
    
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert response.get_json() == expected_response

def test_create_task(client):
    appService = AppService()
    new_task = {
        'id': 4,
        'name': 'task4',
        'description': 'This is task 4'
    }
    expected_response = appService.create_task(new_task)
    
    response = client.post('/api/task', json=new_task)
    assert response.status_code == 200
    assert response.get_json() == expected_response

# Similarly, write tests for update_task and delete_task routes

def test_update_task(client):
    appService = AppService()
    updated_task = {
        'id': 1,
        'name': 'task1_updated',
        'description': 'This is the updated task 1'
    }
    expected_response = appService.update_task(updated_task)
    
    response = client.put('/api/task', json=updated_task)
    assert response.status_code == 200
    assert response.get_json() == expected_response

def test_delete_task(client):
    appService = AppService()
    task_id_to_delete = 1
    expected_response = appService.delete_task(task_id_to_delete)
    
    response = client.delete(f'/api/task/{task_id_to_delete}')
    assert response.status_code == 200
    assert response.get_json() == expected_response
