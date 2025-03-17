import logging

import allure
import requests
from requests import Response

logging.basicConfig(level=logging.INFO)




class BaseApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("GET request to {endpoint}")
    def get(self, endpoint: str, expected_status_code=None, **kwargs) -> Response:
        response = requests.get(f"{self.base_url}{endpoint}", **kwargs)
        logging.info(f"Sending GET request to {self.base_url}{endpoint}")
        return response if expected_status_code == response.status_code else _handle_error(response)

    @allure.step("POST request to {endpoint}")
    def post(self, endpoint: str, expected_status_code=None, **kwargs) -> Response:
        response = requests.post(f"{self.base_url}{endpoint}", **kwargs)
        logging.info(f"Sending POST request to {self.base_url}{endpoint}")
        return response if expected_status_code == response.status_code  else _handle_error(expected_status_code, response)

def _handle_error(expected_status_code:int,  response:Response) -> None:
    logging.error(f"Expected status code: {expected_status_code}, but was {response.status_code}")
    raise Exception(f"Expected status code: {expected_status_code}, but was {response.status_code}")
