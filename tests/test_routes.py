import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"ACEest Fitness & Gym" in response.data

def test_add_workout(client):
    response = client.post('/add', data={'workout': 'Pushups', 'duration': '15'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Pushups" in response.data

def test_view_workouts(client):
    client.post('/add', data={'workout': 'Squats', 'duration': '20'}, follow_redirects=True)
    response = client.get('/view')
    assert response.status_code == 200
    assert b"Squats" in response.data

def test_add_workout_empty_fields(client):
    response = client.post('/add', data={'workout': '', 'duration': ''}, follow_redirects=True)
    assert b"Please enter both workout and duration." in response.data

def test_add_workout_invalid_duration(client):
    response = client.post('/add', data={'workout': 'Yoga', 'duration': 'abc'}, follow_redirects=True)
    assert b"Duration must be a number." in response.data

def test_multiple_workouts(client):
    client.post('/add', data={'workout': 'Running', 'duration': '30'}, follow_redirects=True)
    client.post('/add', data={'workout': 'Cycling', 'duration': '45'}, follow_redirects=True)
    response = client.get('/view')
    assert b"Running" in response.data
    assert b"Cycling" in response.data


