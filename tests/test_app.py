import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200


def test_create_short_url(client):
    response = client.post(
        "/",
        data={"original_url": "https://www.google.com"}
    )

    assert response.status_code == 200
    assert b"http://localhost/" in response.data


def test_redirect_short_url(client):
    response = client.post(
        "/",
        data={"original_url": "https://www.google.com"}
    )

    short_url = response.text.split('href="')[1].split('"')[0]
    short_code = short_url.rstrip("/").split("/")[-1]

    response = client.get("/" + short_code)

    assert response.status_code == 302
    assert response.location == "https://www.google.com"
def test_invalid_short_url(client):
    response = client.get("/DOESNOTEXIST")

    assert response.status_code == 200
    assert b"Short URL Not Found" in response.data