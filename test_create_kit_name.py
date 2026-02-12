import pytest
import sender_stand_request
from data import get_user_body, get_kit_body


def get_auth_token():
    user_body = get_user_body()
    response = sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]


def create_kit(name):
    token = get_auth_token()
    body = get_kit_body(name)
    return sender_stand_request.post_new_kit(body, token)


def test_create_kit_name_1_symbol():
    response = create_kit("a")
    assert response.status_code == 201
    assert response.json()["name"] == "a"


def test_create_kit_name_511_symbols():
    name = "A" * 511
    response = create_kit(name)
    assert response.status_code == 201
    assert response.json()["name"] == name


def test_create_kit_name_0_symbols():
    response = create_kit("")
    assert response.status_code == 400


def test_create_kit_name_512_symbols():
    name = "A" * 512
    response = create_kit(name)
    assert response.status_code == 400


@pytest.mark.parametrize("name", [
    "QWErty",
    "Мария",
    "!@#№%",
    " Человек и КО ",
    "123"
])
def test_create_kit_valid_symbols(name):
    response = create_kit(name)
    assert response.status_code == 201
    assert response.json()["name"] == name


def test_create_kit_without_name():
    token = get_auth_token()
    response = sender_stand_request.post_new_kit({}, token)
    assert response.status_code == 400


def test_create_kit_name_number():
    token = get_auth_token()
    response = sender_stand_request.post_new_kit({"name": 123}, token)
    assert response.status_code == 400