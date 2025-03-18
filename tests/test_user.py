import allure
import pytest

from assertions.assertions import compare_dicts
from base.user_client import UserClient
from models.user_request import UserRequest


@pytest.mark.user
@allure.feature('User')
@allure.story('PetStore API')
class TestUser:
    @allure.title("Create User")
    def test_user_creation(self, user_client: UserClient, user_request_body: UserRequest):
        response = user_client.create_user(200 , user_request_body)
        compare_dicts(response.json(), user_request_body.model_dump(by_alias=True))


