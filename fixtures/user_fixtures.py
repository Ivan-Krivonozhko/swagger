import pytest

from base.user_client import UserClient
from models.user_request import UserRequest
from utils.test_data import TestData



"""
Fixtures returns UserClient
:return UserClient
"""
@pytest.fixture(scope="class")
def user_client() -> UserClient:
    return UserClient()

"""
Fixtures returns random UserRequest

:return UserRequest
"""
@pytest.fixture(scope="function")
def user_request_body() -> UserRequest:
    test_data = TestData()
    return UserRequest(id=test_data.random_number(10, 1000),
                       firstName=test_data.random_first_name(),
                       lastName=test_data.random_last_name(),
                       email=test_data.random_email(),
                       password=test_data.random_password(),
                       userStatus=test_data.random_number(1, 100))
