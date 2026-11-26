import requests

url_get = "https://postman-echo.com/get"
url_post = "https://postman-echo.com/post"


def test_get_postman_url_with_query_params(postman_user_name):

    response = requests.get(url_get, params=postman_user_name)
    body = response.json()

    assert response.status_code == 200
    assert body["args"] == postman_user_name


def test_get_postman_url_with_incorrect_method():
    response = requests.post(url_get)

    assert response.status_code == 404
    assert response.text == ""


def test_get_postman_url_with_query_params_and_body(postman_user_name, postman_body):

    response = requests.get(url_get, params=postman_user_name, json=postman_body)
    body = response.json()

    assert response.status_code == 200
    assert body["args"] == postman_user_name | postman_body

def test_post_postman_url_with_query_params_and_body(postman_user_name, postman_body):

    response = requests.post(url_post, params=postman_user_name, json=postman_body)
    body = response.json()

    assert response.status_code == 200
    assert body["args"] == postman_user_name
    assert body["data"] == postman_body

def test_post_postman_url_with_file():
    with open("tests/test.txt", "rb") as file:
        files = {"document":file}
        response = requests.post(url_post, files=files)

    assert response.status_code == 200
    assert "test.txt" in response.json()["files"]