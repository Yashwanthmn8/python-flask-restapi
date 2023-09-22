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
    # Assuming you have a method in AppService to return tasks
    expected_response = client.get('/api/tasks')
    
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert response.get_json() == expected_response

# Similarly, write tests for create_task, update_task, and delete_task routes
# Make sure to test both success and error cases for each route.
