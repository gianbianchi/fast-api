from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app


def test_read_root_must_return_ok_and_hello_world():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"Hello": "World"}
