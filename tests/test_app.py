from app.main import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"Hello from Flask Docker CI/CD!"