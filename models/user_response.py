from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    code: int = Field()
    type: str =  Field()
    message: str =  Field()
