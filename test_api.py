import pytest
import requests


def test_get_post_check_user_id():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    assert response.json()["userId"] == 1


def test_create_post_check_status_code():
    url = "https://jsonplaceholder.typicode.com/posts"

    new_post_data = {
        "title": "pytest test title",
        "body": "pytest test body content",
        "userId": 5,
    }

    response = requests.post(url, json=new_post_data, timeout=10)

    assert response.status_code == 201
    assert response.json()["title"] == new_post_data["title"]


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_multiple_posts_status_code(base_url, post_id):
    url = f"{base_url}/posts/{post_id}"

    response = requests.get(url, timeout=10)

    assert response.status_code == 200
    assert response.json()["id"] == post_id
