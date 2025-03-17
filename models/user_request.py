from pydantic import BaseModel, Field

from utils.test_data import TestData
test_data = TestData()

class UserRequest(BaseModel):
    id: int = Field(default=TestData.random_number(1, 1000))
    first_name: str =  Field(default=test_data.random_first_name(), alias="firstName")
    last_name: str =  Field(default=test_data.random_last_name(), alias="lastName")
    email: str = Field(default=test_data.random_email(), alias="email")
    password: str = Field(default=test_data.random_password(), alias="password")
    user_status: int = Field(default=test_data.random_number(1, 1000), alias="userStatus")

