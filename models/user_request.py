from pydantic import BaseModel, Field



class UserRequest(BaseModel):
    id: int = Field()
    first_name: str =  Field(alias="firstName")
    last_name: str =  Field(alias="lastName")
    email: str = Field(alias="email")
    password: str = Field(alias="password")
    user_status: int = Field(alias="userStatus")

