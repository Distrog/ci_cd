import pytest


@pytest.fixture
def postman_user_name():
    return {"name": "Dmitriy"}


@pytest.fixture
def postman_body():
    return {"test": "test"}
