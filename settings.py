
from pydantic_settings import BaseSettings, SettingsConfigDict


class TestUser(BaseSettings):
    id: int = 0
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    password: str = ""
    phone: str = ""
    user_status: int = 0


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    base_url: str
    user: TestUser = TestUser()

    @property
    def api_url(self) -> str:
        return f'{self.base_url}'


base_settings = Settings()