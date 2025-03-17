import pytest


from base.user_client import UserClient
from models.user_request import UserRequest


@pytest.fixture(scope="class")
def user_client() -> UserClient:
     user_client = UserClient()
     return user_client

@pytest.fixture(scope="function")
def user_request_body() -> UserRequest:
     return UserRequest()