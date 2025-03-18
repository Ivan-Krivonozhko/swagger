import logging
from enum import StrEnum

import allure

from base.base_api_client import BaseApiClient
from constants.routes import Routes
from models.user_request import UserRequest
from settings import base_settings



class UserClient(BaseApiClient):
    def __init__(self):
        super().__init__(base_settings.base_url)

    @allure.step("Create user")
    def create_user(self, expected_status_code:int, payload:UserRequest):
        logging.info(f"Create user: {payload}")
        return self.post(Routes.USER.value,
                         expected_status_code=expected_status_code,
                         json=payload.model_dump(by_alias=True),
                         headers={"Content-Type": "application/json"})